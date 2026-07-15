import streamlit as st

from graph import graph

st.set_page_config(
    page_title="AI PDF ChatBot",
    page_icon="📚",
    layout="wide"
)

st.title("LangGraph RAG Chatbot")
st.markdown("Ask questions about your PDF documents. ")

st.markdown("---")

#session state

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

#user input

question=st.text_area(
    "Ask a question about your documents",
    height=120,
    placeholder="Example: Explain Inconsistency"
)

if st.button("Generate Answer"):
    
    if question.strip()=="":
        st.warning("Please enter a question.")

    else:
        with st.spinner("Searching documents"):
            response=graph.invoke(
                {
                    "question":question,
                    "chat_history":st.session_state.chat_history
                }
            )

        #save chat history

        st.session_state.chat_history.append(
            (
                question,
                response["answer"]
            )
        )

        #Answer-------------------------------------------------------

        st.markdown("## Answer")

        st.write(response["answer"])

        #Sources-------------------------------------------------------

        st.markdown("---")
        st.subheader("📄 Sources")

        sources=set()

        for doc in response["documents"]:
            source=(
                doc.metadata.get("source"),
                doc.metadata.get("page")
            )

            sources.add(source)

        for source,page in sorted(sources):
            st.write(f"**{source}**  (Page{page})")

#prev conversation---------------------------------

if st.session_state.chat_history:
    st.markdown("---")
    st.subheader("💬 Conversation History")

    for i ,(user,assistant) in enumerate(st.session_state.chat_history,start=1):
        with st.expander(f"Conversation {i}"):
            st.markdown(f"**👨‍🦰 You:** {user}")

            st.markdown(f"**🤖 Assistant:** {assistant}")
