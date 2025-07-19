from vectorstore import load_vectorstore

def generate_answer(query):
    data, embeddings, faiss_index = load_vectorstore()

    # Search similar entries
    results = faiss_index.similarity_search(query, k=3)

    if results:
        response = "\n\n".join([doc.page_content for doc in results])
    else:
        response = "Sorry, I couldn't find information related to your query."

    return response
