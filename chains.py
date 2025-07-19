from vectorstore import load_vectorstore
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json

model = SentenceTransformer('all-MiniLM-L6-v2')

# Load vectorstore and metadata
docs, vectors = load_vectorstore()


def generate_answer(query):
    query_vec = model.encode([query])
    similarities = cosine_similarity(query_vec, vectors)[0]
    top_k = np.argsort(similarities)[-3:][::-1]
    
    response = ""
    for idx in top_k:
        response += f"### {docs[idx]['name']}\n{docs[idx]['content']}\n\n"
    
    return response
