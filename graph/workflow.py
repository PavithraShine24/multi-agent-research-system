from langgraph.graph import StateGraph, START, END

from models.state import AppState
from graph.nodes import research_node, writer_node


def build_graph():

    workflow = StateGraph(AppState)

    workflow.add_node("research", research_node)
    workflow.add_node("writer", writer_node)

    workflow.add_edge(START, "research")
    workflow.add_edge("research", "writer")
    workflow.add_edge("writer", END)

    return workflow.compile()