import streamlit as st

from graph import graph

st.set_page_config(
    page_title="AI PDF ChatBot",
    page_icon="📚",
    layout="wide"
)

st.title("LangGraph RAG Chatbot")

st.markdown("---")

question=st.text_area(
    "Ask a question about your documents",
    height=120,
    placeholder="Example: Explain Incons"
)

if st.button("Generate Answer"):
    
    if question.strip()=="":
        st.warning("Please enter a question.")

    else:
        with st.spinner("Searching documents"):
            response=graph.invoke(
                {
                    "question":question
                }
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