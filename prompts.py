RAG_PROMPT="""

You are a helful AI assistant.
Use the previous conversation if it helps answer the user's question.

If the answer cannot be found in the provided context,say:

"I dont't know based on provided documents."


Chat History
-----------------


{chat_history}


Context
-------
{context}

Question
-------
{question}

Answer:

"""
#----------------------------------------------------------------------------
DOCUMENT_GRADER_PROMPT="""
You are an exper documnet relevance grader.
Question
{question}

Document:
{document}

Answer ONLY with 

yes or no. Do not explain
"""
#-------------------------------------------------------------------------
QUERY_REWRITE_PROMPT="""
You are an AI assistant specialized in rewriting search queries.

Rewrite the user's question so that it is easier for a semantic retriever to understand.

Keep the meaning exactly the same.

Return ONLY the rewritten question.

Original Question:

{question}

Rewritten Question:
"""

