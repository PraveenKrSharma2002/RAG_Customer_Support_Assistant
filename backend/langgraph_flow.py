from typing import TypedDict

from langgraph.graph import StateGraph, END


class GraphState(TypedDict):

    query: str

    answer: str


def process_node(state):

    query = state["query"]

    answer = f"Processing Query: {query}"

    return {
        "query": query,
        "answer": answer
    }


builder = StateGraph(GraphState)

builder.add_node("process", process_node)

builder.set_entry_point("process")

builder.add_edge("process", END)

graph = builder.compile()