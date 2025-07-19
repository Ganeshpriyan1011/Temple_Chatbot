import json
import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def load_vectorstore():
    with open("temple.json", "r", encoding="utf-8") as f:
        temple_data = json.load(f)

    model = SentenceTransformer('all-MiniLM-L6-v2')

    texts = []
    metadata = []

    for temple in temple_data:
        content = f"{temple['name']} located at {temple['location']}. Mythology: {temple['mythology']}. Architecture: {temple['architecture']}"
        texts.append(content)
        metadata.append(temple)

    embeddings = model.encode(texts)
    return metadata, embeddings, model
