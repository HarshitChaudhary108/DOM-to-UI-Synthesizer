from agent.nodes.common import fast_llm, structured_invoke
from agent.state.schemas import DesignSpec
from prompt import SPEC_SYSTEM


def spec_node(state: dict) -> dict:
    spec = structured_invoke(fast_llm, [
        ("system", SPEC_SYSTEM),
        ("user", f"URL: {state['url']}\n\nCAPTURE:\n{state['dom']}"),
    ], DesignSpec)
    print(f"  spec: {len(spec.sections)} sections, primary={spec.primary_color}")
    return {"spec": spec.model_dump()}