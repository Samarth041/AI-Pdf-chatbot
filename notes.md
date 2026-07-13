# AI PDF Chatbot Project Structure

```text
AI-PDF-Chatbot/
│
├── app.py                  # Streamlit UI for users
├── config.py               # Load environment variables and project configuration
├── graph.py                # Build and compile the LangGraph workflow
├── nodes.py                # Graph node implementations (retrieve, generate, etc.)
├── state.py                # Shared LangGraph state definition
├── retriever.py            # Load persisted ChromaDB and create the retriever
├── ingest.py               # Read PDFs, chunk text, create embeddings, store in ChromaDB
├── prompts.py              # Prompt templates used by the LLM
├── utils.py                # Utility/helper functions
│
├── data/                   # Input PDF files
│   └── sample.pdf
│
├── chroma_db/              # Persisted Chroma vector database
│
├── .env                    # API keys and environment variables
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Files/folders to ignore in Git
```

---

## File Responsibilities

| File | Responsibility |
|------|----------------|
| **config.py** | Load environment variables and project configuration |
| **ingest.py** | Read PDFs, split into chunks, create embeddings, and save them to ChromaDB |
| **retriever.py** | Load the persisted ChromaDB and expose a retriever |
| **state.py** | Define the shared state that flows through the LangGraph |
| **nodes.py** | Implement graph nodes such as retrieval and answer generation |
| **graph.py** | Connect the nodes into a LangGraph workflow |
| **app.py** | Build the Streamlit user interface |
| **prompts.py** | Store reusable prompt templates |
| **utils.py** | Common helper functions used across the project |

---

## Workflow

```text
PDF Documents
      │
      ▼
ingest.py
(Read → Chunk → Embed)
      │
      ▼
ChromaDB
(Persisted Vector Store)
      │
      ▼
retriever.py
      │
      ▼
LangGraph
(graph.py)
      │
 ┌────┴────┐
 ▼         ▼
Retrieve   Generate
(nodes.py)
      │
      ▼
Final Answer
      │
      ▼
Streamlit UI
(app.py)
```