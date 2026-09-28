from typing import TypedDict, Literal


class AgentState(TypedDict, total=False):
    mode: Literal["clone", "modify"]
    url: str
    dom: str              # compact JSON string from Playwright
    spec: dict            # DesignSpec.model_dump()
    files: dict[str, str] # path -> content (current source of truth)
    build_ok: bool
    build_log: str
    retries: int
    instruction: str