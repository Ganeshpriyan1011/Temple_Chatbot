import json
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS


def load_vectorstore():
    with open("temple.json", "r", encoding="utf-8") as f:
        temples = json.load(f)

    data = []
    for temple in temples:
        name = temple.get("temple_name", "Unknown Temple")
        location = temple.get("location", "Unknown Location")
        deity = temple.get("deity", "Unknown Deity")
        mythology = temple.get("mythology", "No mythology available")
        
        arch = temple.get("architecture", {})
        style = arch.get("style", "Unknown style")
        era = arch.get("era", "Unknown era")
        materials = arch.get("materials", "Unknown materials")
        features = arch.get("features", "No architectural features")

        content = (
            f"{name}, located at {location}, is dedicated to {deity}. "
            f"Mythology: {mythology}. "
            f"Architecture: Style - {style}, Era - {era}, Materials - {materials}, Features - {features}."
        )

        data.append(content)

    embeddings = SentenceTransformer("all-MiniLM-L6-v2")
    model = FAISS.from_texts(data, embeddings)

    return data, embeddings, model
