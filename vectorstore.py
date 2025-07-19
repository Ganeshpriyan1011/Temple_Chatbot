from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.docstore.document import Document
import json

def load_vectorstore():
    with open("temple.json", "r", encoding="utf-8") as file:
        temple_data = json.load(file)

    # Prepare list of strings from the JSON
    data = []
    for temple in temple_data:
        content = f"""
        Temple Name: {temple['temple_name']}
        Location: {temple['location']}
        Deity: {temple['deity']}
        Mythology: {temple['mythology']}
        Architecture Style: {temple['architecture']['style']}
        Architecture Features: {temple['architecture']['features']}
        """
        data.append(content.strip())

    # Use LangChain's HuggingFaceEmbeddings wrapper
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create FAISS index
    model = FAISS.from_texts(data, embedding=embeddings)

    return data, embeddings, model
