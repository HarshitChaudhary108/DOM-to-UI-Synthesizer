from langgraph.graph import StateGraph, START, END
from agent.state.agent_state import AgentState
from agent.nodes.common import MAX_RETRIES
from agent.nodes.scrape import scrape_node
from agent.nodes.spec import spec_node
from agent.nodes.codegen import codegen_node
from agent.nodes.validate import validate_node, fix_node
from agent.nodes.modify import modify_node


def route_start(state: AgentState) -> str:
    return "modify" if state.get("mode") == "modify" else "scrape"


def route_after_validate(state: AgentState) -> str:
    if state["build_ok"]:
        return END
    return "fix" if state.get("retries", 0) < MAX_RETRIES else END


def build_graph():
    g = StateGraph(AgentState)
    g.add_node("scrape", scrape_node)
    g.add_node("spec", spec_node)
    g.add_node("codegen", codegen_node)
    g.add_node("validate", validate_node)
    g.add_node("fix", fix_node)
    g.add_node("modify", modify_node)

    g.add_conditional_edges(START, route_start, ["scrape", "modify"])
    g.add_edge("scrape", "spec")
    g.add_edge("spec", "codegen")
    g.add_edge("codegen", "validate")
    g.add_edge("modify", "validate")
    g.add_conditional_edges("validate", route_after_validate, ["fix", END])
    g.add_edge("fix", "validate")
    return g.compile()