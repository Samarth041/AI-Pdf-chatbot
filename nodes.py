from retriever import retrieve_documents
from prompts import DOCUMENT_GRADER_PROMPT
from prompts import RAG_PROMPT
from utils import chat_model

from prompts import QUERY_REWRITE_PROMPT

def retrieve(state):
    question=state["question"]

    docs=retrieve_documents(question)

    return{
        "question":question,
        "documents":docs
    }

def generate(state):

    question=state["question"]

    docs=state["filtered_documents"]

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

#GRADE DOCUMENT node

def grade_documents(state):

    question=state["question"]

    docs=state["documents"]

    relevant_docs=[]

    for doc in docs:
        prompt=DOCUMENT_GRADER_PROMPT.format(
            question=question,
            document=doc.page_content
        )

        response=chat_model.invoke(prompt)

        if "yes" in response.content.lower():
            relevant_docs.append(doc)

    return{
        "filtered_documents":relevant_docs
    }


def rewrite_query(state):
    question=state["question"]

    prompt=QUERY_REWRITE_PROMPT.format(
        question=question
    )

    response=chat_model.invoke(prompt)

    rewritten_question=response.content.strip()

    return {
        "question":rewritten_question
    }

def decide_to_generate(state):
    docs=state["filtered_documents"]

    if len(docs)==0:

        return "rewrite"
    return "generate"