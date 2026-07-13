import os
from pathlib import Path


from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


DOCUMENTS_DIR="documents"
VECTORSTORE_DIR="vectorstore"

EMBEDDING_MODEL="BAAI/bge-small-en-v1.5"

#loaing Embedding model

embedding_model=HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

#load PDFs

def load_documents():
    documents=[]

    pdf_files=Path(DOCUMENTS_DIR).glob("*.pdf")

    for pdf in pdf_files:
        print(f"Loading{pdf.name}")

        loader=PyPDFLoader(str(pdf))

        docs=loader.load()

        #add filename as metadata

        for doc in docs:
            doc.metadata["source"]=pdf.name

        documents.extend(docs)

    return documents


#split documents

def split_documents(documents):
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=200,
        separators=["\n\n","\n",".",""," "]
    )

    chunks=splitter.split_documents(documents)

    print(f"created {len(chunks)} chunks")

    return chunks

#create vector store

def create_vectorstore(chunks):
    db=Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=VECTORSTORE_DIR
    )

    print("Vector DB created successfully")

    return db

#main

def main():
    print("-"*50)
    print("Loading PDFs....")
    print("-"*50)

    docs=load_documents()

    print(f"loaded {len(docs)} pages")

    print()

    print("-"*50)

    chunks=split_documents(docs)

    print()

    print("-"*50)

    print("Creating Vector Store")

    print("-"*50)

    create_vectorstore(chunks)
    print()

    print("Finished")

if __name__=="__main__":
    main()


    
