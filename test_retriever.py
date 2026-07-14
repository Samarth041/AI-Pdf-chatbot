from retriever import retrieve_documents

question="Explain Inconsistency"

docs=retrieve_documents(question)

print("-"*60)

for i, doc in enumerate(docs):
    print("\n Document {i+1}\n")

    print(doc.page_content[:500])

    print("\nMetadata")

    print(doc.metadata)

    print("-"*60)