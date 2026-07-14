from retriever import retrieve_documents

from prompts import RAG_PROMPT
from utils import chat_model

def retrieve(state):
    question=state["question"]

    docs=retrieve_documents(question)

    return{
        "question":question,
        "documents":docs
    }

def generate(state):

    question=state["question"]

    docs=state["documents"]

    context="\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt=RAG_PROMPT.format(
        context=context,
        question=question
    )

    response=chat_model.invoke(prompt)

    return {
        "answer":response.content
    }