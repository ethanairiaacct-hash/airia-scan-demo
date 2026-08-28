"""Multi-step research graph."""
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4.1", temperature=0)


class ResearchState(TypedDict):
    messages: Annotated[list, add_messages]
    depth: int


def plan(state: ResearchState) -> ResearchState:
    return {"messages": [model.invoke(state["messages"])], "depth": state["depth"] + 1}


def should_continue(state: ResearchState) -> str:
    return "plan" if state["depth"] < 3 else END


builder = StateGraph(ResearchState)
builder.add_node("plan", plan)
builder.add_edge(START, "plan")
builder.add_conditional_edges("plan", should_continue)
graph = builder.compile()
