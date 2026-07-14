from graph import graph
response=graph.invoke(
    {
        "question":"Explain Hallucination"
    }
)

print()

print(response["answer"])