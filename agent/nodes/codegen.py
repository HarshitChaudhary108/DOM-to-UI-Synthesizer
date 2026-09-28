import json
from agent.nodes.common import code_llm, apply_output, read_site, reset_components, structured_invoke
from agent.state.schemas import CodeOutput
from prompt import CODEGEN_SYSTEM


def codegen_node(state: dict) -> dict:
    structured = code_llm.with_structured_output(CodeOutput, method="json_schema")
    out = structured_invoke(code_llm, [
    ("system", CODEGEN_SYSTEM),
    ("user", "DesignSpec:\n" + json.dumps(state["spec"], indent=1)),
    ], CodeOutput)
    reset_components()
    apply_output(out)
    files = read_site()
    print(f"  wrote {len(files)} files")
    return {"files": files, "retries": 0}