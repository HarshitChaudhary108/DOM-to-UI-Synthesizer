import json
from agent.nodes.common import code_llm, apply_output, read_site
from agent.state.schemas import CodeOutput
from prompt import MODIFY_SYSTEM


def modify_node(state: dict) -> dict:
    structured = code_llm.with_structured_output(CodeOutput, method="json_schema")
    out: CodeOutput = structured.invoke([
        ("system", MODIFY_SYSTEM),
        ("user", f"INSTRUCTION: {state['instruction']}\n\nCURRENT FILES:\n{json.dumps(read_site())}"),
    ])
    apply_output(out)
    print(f"  changed {[f.path for f in out.files]}, deleted {out.deleted}")
    return {"files": read_site(), "retries": 0}