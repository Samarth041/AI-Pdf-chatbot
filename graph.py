from langgraph.graph import StateGraph,START,END

from state import GraphState
from nodes import retrieve,generate,grade_documents

builder=StateGraph(GraphState)

builder.add_node("retrieve",retrieve)
builder.add_node("grade_documents",grade_documents)
builder.add_node("generate",generate)

builder.set_entry_point("retrieve")

builder.add_edge("retrieve","grade_documents")
builder.add_edge("grade_documents","generate")

builder.add_edge("generate",END)

graph=builder.compile()