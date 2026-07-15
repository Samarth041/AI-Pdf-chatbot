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

    history=state.get("chat_history",[])

    context="\n\n".join(
        doc.page_content
        for doc in docs
    )

    history_text=""

    for human,ai in history:
        history_text+=f"Human: {human}\n"

        history_text+=f"Assistant: {ai}\n\n"

    prompt=RAG_PROMPT.format(
        chat_history=history_text,
        context=context,
        question=question
    )

    response=chat_model.invoke(prompt)

    return {
        "answer":response.content
    }