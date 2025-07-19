from vectorstore import load_vectorstore
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def generate_answer(query):
    data, embeddings, model = load_vectorstore()
    query_embedding = model.encode([query])
    scores = cosine_similarity(query_embedding, embeddings)[0]

    best_idx = np.argmax(scores)
    best_match = data[best_idx]

    return f"""
    📍 **Temple Name**: {best_match['name']}
    🗺️ **Location**: {best_match['location']}
    🕉️ **Mythology**: {best_match['mythology']}
    🏛️ **Architecture**: {best_match['architecture']}
    """
