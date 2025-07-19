import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer

def load_vectorstore():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    data = []
    embeddings = []

    for filename in os.listdir("temples"):
        if filename.endswith(".json"):
            with open(os.path.join("temples", filename), "r", encoding="utf-8") as f:
                temple = json.load(f)
                content = f"{temple['name']} {temple['mythology']} {temple['architecture']}"
                data.append(temple)
                embeddings.append(model.encode(content))

    return data, np.array(embeddings), model
