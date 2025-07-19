from vectorstore import load_vectorstore
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def generate_answer(query):
    data, embeddings, model = load_vectorstore()
    query_embedding = model.encode([query])
    sims = cosine_similarity(query_embedding, embeddings)[0]
    best_match = data[np.argmax(sims)]
    return f"**Mythology**: {best_match['mythology']}\n\n**Architecture**: {best_match['architecture']}"
