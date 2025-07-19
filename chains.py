from vectorstore import load_vectorstore

def generate_answer(query, score_threshold=0.4):
    data, embeddings, faiss_index = load_vectorstore()

    results_with_scores = faiss_index.similarity_search_with_score(query, k=5)

    # Filter based on score (lower is better)
    filtered_results = [
        doc for doc, score in results_with_scores if score < score_threshold
    ]

    if filtered_results:
        response = "\n\n".join([doc.page_content for doc in filtered_results])
    else:
        response = "Sorry, I couldn't find information related to your query."

    return response
