import os
import json
import re
import time
import shutil
from pathlib import Path
from langchain_groq import ChatGroq
from agent.state.schemas import CodeOutput
from groq import BadRequestError
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
SITE = Path("site")
MAX_RETRIES = 3

fast_llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.5,
                    reasoning_effort="low", max_tokens=3000, max_retries=3, api_key=os.getenv("GROQ_API_KEY"))
code_llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.5,
                    reasoning_effort="low", max_tokens=6000, max_retries=3, api_key=os.getenv("GROQ_API_KEY"))


def _strictify(s):
    """Make any Pydantic JSON schema comply with Groq strict mode:
    every property required, every object closed, no default/title keywords."""
    if isinstance(s, list):
        return [_strictify(x) for x in s]
    if not isinstance(s, dict):
        return s
    s = {k: v for k, v in s.items() if k not in ("default", "title")}
    if "properties" in s:
        s["properties"] = {k: _strictify(v) for k, v in s["properties"].items()}
        s["required"] = list(s["properties"])
        s["additionalProperties"] = False
    for k in ("items", "anyOf", "allOf", "oneOf"):
        if k in s:
            s[k] = _strictify(s[k])
    if "$defs" in s:
        s["$defs"] = {k: _strictify(v) for k, v in s["$defs"].items()}
    return s


def structured_invoke(llm, messages: list, model_cls: type[BaseModel], attempts: int = 3):
    """Strict JSON-schema call with retries. The last attempt drops response_format entirely
    (plain text + JSON extraction), which cannot trigger json_validate_failed."""
    schema = _strictify(model_cls.model_json_schema())
    response_format = {"type": "json_schema",
                       "json_schema": {"name": model_cls.__name__, "strict": True, "schema": schema}}
    last: Exception | None = None
    for i in range(attempts):
        try:
            if i < attempts - 1:
                resp = llm.invoke(messages, response_format=response_format)
            else:
                resp = llm.invoke(messages + [(
                    "user",
                    "Return ONLY one JSON object matching this JSON Schema. "
                    "No prose, no code fences:\n" + json.dumps(schema))])
            text = resp.content if isinstance(resp.content, str) else ""
            if not text.strip():
                raise ValueError(f"empty completion (finish_reason={resp.response_metadata.get('finish_reason')})")
            m = re.search(r"\{.*\}", text, re.S)
            return model_cls.model_validate_json(m.group(0) if m else text)
        except (BadRequestError, ValueError) as e:      # pydantic ValidationError is a ValueError
            last = e
            print(f"  [structured retry {i + 1}/{attempts}] {type(e).__name__}: {str(e)[:120]}")
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"structured output failed after {attempts} attempts") from last

def safe_path(rel: str) -> Path | None:
    """Only allow components/*.tsx and app/page.tsx, block path traversal."""
    rel = rel.replace("//", "/").lstrip("/")
    ok = rel == "app/page.tsx" or (rel.startswith("components/") and rel.endswith(".tsx"))
    if not ok:
        return None
    p = (SITE / rel).resolve()
    return p if SITE.resolve() in p.parents else None


def apply_output(out: CodeOutput) -> None:
    for f in out.files:
        p = safe_path(f.path)
        if p is None:
            print(f"  [skip] disallowed path: {f.path}")
            continue
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f.content, encoding="utf-8")
    for d in out.deleted:
        p = safe_path(d)
        if p:
            p.unlink(missing_ok=True)


def read_site() -> dict[str, str]:
    files = {}
    page = SITE / "app" / "page.tsx"
    if page.exists():
        files["app/page.tsx"] = page.read_text(encoding="utf-8")
    for p in (SITE / "components").glob("**/*.tsx"):
        files[p.relative_to(SITE).as_posix()] = p.read_text(encoding="utf-8")
    return files


def reset_components() -> None:
    shutil.rmtree(SITE / "components", ignore_errors=True)