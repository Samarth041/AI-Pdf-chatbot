from langchain_groq import ChatGroq
from config import GROQ_API_KEY

chat_model = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0.2,
)