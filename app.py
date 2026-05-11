from backend.loader import load_pdf

from backend.splitter import split_documents

from backend.embeddings import create_vector_store

from backend.retriever import get_retriever

from backend.rag_chain import generate_answer

from backend.hitl import check_escalation


print("Loading PDF...")

docs = load_pdf("data/company_policy.pdf")


print("Splitting PDF into chunks...")

chunks = split_documents(docs)


print("Creating Vector Database...")

vectorstore = create_vector_store(chunks)


retriever = get_retriever(vectorstore)


print("\nRAG Customer Support Assistant Ready!\n")


while True:

    query = input("Ask Your Question: ")

    if query.lower() == "exit":
        break

    retrieved_docs = retriever.invoke(query)

    answer = generate_answer(query, retrieved_docs)

    escalation = check_escalation(answer)

    print("\nAnswer:\n")

    print(answer)

    if escalation:

        print("\nEscalated to Human Support Agent")