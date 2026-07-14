from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

#configuration

VECTORSTORE_DIR="vectorstore"
EMBEDDING_MODEL="BAAI/bge-small-en-v1.5"

#LOad embedding model

embedding_model=HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

#load existing Chroma DataBase

vectorstore=Chroma(
    persist_directory=VECTORSTORE_DIR,
    embedding_function=embedding_model
)

#retriever

retriever=vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k":4,
        "fetch_k":10,
        "lambda_mult":0.7
    }
)

#function 

def retrieve_documents(question:str):
    documents=retriever.invoke(question)

    return documents