# RAG Customer Support Assistant

An AI-powered Customer Support Assistant built using Python, Streamlit, LangGraph, and Retrieval-Augmented Generation (RAG) concepts.

This project is designed to simulate a real-world customer support system where users can upload company policy PDF documents and ask questions related to refunds, leave policies, work-from-home rules, security guidelines, and customer support information.

The assistant retrieves relevant information from uploaded documents and generates contextual answers based on the document content. It also supports Human-in-the-Loop (HITL) escalation for unsupported or low-confidence queries.

## Features

- Dynamic PDF Upload Support
- PDF Text Extraction
- Document Chunking
- Retrieval-Based Question Answering
- Context-Aware Responses
- Human-in-the-Loop (HITL) Escalation
- Streamlit Interactive UI
- Modular Backend Architecture
- LangGraph Workflow Integration

## Tech Stack

- Python
- Streamlit
- LangChain
- LangGraph
- PyPDFLoader
- ChromaDB

## Project Workflow

1. User uploads a company policy PDF.
2. The system extracts text from the document.
3. The document is split into smaller chunks.
4. Relevant chunks are retrieved based on the user query.
5. The system generates a contextual answer.
6. Unsupported queries can be escalated using HITL logic.

## Project Structure

```bash
RAG_Customer_Support_Assistant/
│
├── backend/
│   ├── loader.py
│   ├── splitter.py
│   ├── retriever.py
│   ├── rag_chain.py
│   ├── hitl.py
│   └── langgraph_flow.py
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
│   └── company_policy.pdf
│
├── requirements.txt
├── .gitignore
└── README.md
```
## Run Project

- Clone Repository
```bash
git clone https://github.com/PraveenKrSharma2002/RAG_Customer_Support_Assistant.git
```
- Install Dependencies
```bash
pip install -r requirements.txt
```
- Run Streamlit App
```bash
streamlit run frontend/streamlit_app.py
```
## Sample Questions
- What is refund policy?
- How can customer contact support?
- What is work from home policy?

## Author
- Praveen Kumar Sharma
