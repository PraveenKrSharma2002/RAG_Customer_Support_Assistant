def simple_retriever(chunks, query):

    relevant_chunks = []

    query_words = query.lower().split()

    for chunk in chunks:

        text = chunk.page_content.lower()

        for word in query_words:

            if word in text:

                relevant_chunks.append(chunk)

                break

    return relevant_chunks[:3]