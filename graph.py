from langgraph.graph import StateGraph,START,END

from state import GraphState
from nodes import retrieve,generate,grade_documents,rewrite_query,decide_to_generate

builder=StateGraph(GraphState)

builder.add_node("retrieve",retrieve)
builder.add_node("grade_documents",grade_documents)
builder.add_node("rewrite",rewrite_query)
builder.add_node("generate",generate)

builder.set_entry_point("retrieve")

builder.add_edge("retrieve","grade_documents")
#adding conditional edges

builder.add_conditional_edges(
    "grade_documents",

    decide_to_generate,

    {
        "generate":"generate",
        "rewrite":"rewrite"
    }
)

builder.add_edge("rewrite","retrieve")



builder.add_edge("generate",END)

graph=builder.compile()