import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()
collection = client.get_collection("clinic_faq")
model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_context(query: str, k: int = 3):
    embedding = model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[embedding],
        n_results=k
    )

    docs = results["documents"][0]
    sources = [m["id"] for m in results["metadatas"][0]]
    return docs, sources
