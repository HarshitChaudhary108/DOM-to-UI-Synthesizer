import os
import json
import subprocess
from agent.nodes.common import SITE, MAX_RETRIES, code_llm, apply_output, read_site
from agent.state.schemas import CodeOutput
from prompt import FIX_SYSTEM


def validate_node(state: dict) -> dict:
    env = {**os.environ, "DIST_DIR": ".next-build"}   # separate from the dev server's .next
    r = subprocess.run("npm run build", cwd=SITE, shell=True, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=240, env=env)
    ok = r.returncode == 0
    log = "" if ok else (r.stdout + "\n" + r.stderr)[-3000:]   # the real error is at the tail
    print(f"  build {'OK' if ok else 'FAILED'}")
    return {"build_ok": ok, "build_log": log}


def fix_node(state: dict) -> dict:
    structured = code_llm.with_structured_output(CodeOutput, method="json_schema")
    out: CodeOutput = structured.invoke([
        ("system", FIX_SYSTEM),
        ("user", f"BUILD LOG:\n{state['build_log']}\n\nCURRENT FILES:\n{json.dumps(read_site())}"),
    ])
    apply_output(out)
    n = state.get("retries", 0) + 1
    print(f"  fix attempt {n}/{MAX_RETRIES}")
    return {"files": read_site(), "retries": n}