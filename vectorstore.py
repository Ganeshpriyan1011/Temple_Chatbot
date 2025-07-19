import json
import numpy as np
from sentence_transformers import SentenceTransformer

import os

INDEX_FILE = "faiss_index.npy"
META_FILE = "temples.json"


def build_vectorstore():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    with open(META_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    texts = [x['mythology'] + ' ' + x['architecture'] for x in data]
    vectors = model.encode(texts)
    np.save(INDEX_FILE, vectors)
    print("✅ Vectorstore built and saved.")


def load_vectorstore():
    with open(META_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    vectors = np.load(INDEX_FILE)
    return data, vectors
