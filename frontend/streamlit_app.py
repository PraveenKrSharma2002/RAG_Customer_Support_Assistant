import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st

from backend.loader import load_pdf
from backend.splitter import split_documents
from backend.retriever import simple_retriever
from backend.rag_chain import generate_answer
from backend.hitl import check_escalation


st.title("RAG Customer Support Assistant")


uploaded_file = st.file_uploader(
    "Upload Company Policy PDF",
    type="pdf"
)


if uploaded_file is not None:

    # Save uploaded PDF temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Load PDF
    docs = load_pdf("temp.pdf")

    # Split into chunks
    chunks = split_documents(docs)

    # User Query
    query = st.text_input("Ask a Question")

    if query:

        retrieved_docs = simple_retriever(chunks, query)

        answer = generate_answer(query, retrieved_docs)

        escalation = check_escalation(answer)

        st.subheader("Answer")

        st.write(answer)

        if escalation:
            st.error("Escalated to Human Support")