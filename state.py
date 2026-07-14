from typing import TypedDict, List
from langchain_core.documents import Document

class GraphState(TypedDict):
    """state shared across the langgrpah workflow."""

    # user question
    question:str
    #retrieved documents
    documents:List[Document]

    #final answer

    answer:str