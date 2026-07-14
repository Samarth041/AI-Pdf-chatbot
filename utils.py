from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


from config import HF_TOKEN

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    huggingfacehub_api_token=HF_TOKEN,
    task="text-generation",
    max_new_tokens=512,
    temperature=0.2
)

chat_model=ChatHuggingFace(llm=llm)