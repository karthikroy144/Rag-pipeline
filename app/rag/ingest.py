import json
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client(
    Settings(
        persist_directory="chroma_db",
        anonymized_telemetry=False
    )
)

collection = client.get_or_create_collection("clinic_faq")


def ingest_faq():
    with open("data/clinic_info.json") as f:
        data = json.load(f)

    for item in data:
        text = f"Q: {item['question']} A: {item['answer']}"
        embedding = model.encode(text).tolist()

        collection.add(
            documents=[text],
            embeddings=[embedding],
            metadatas=[{"id": item["id"]}],
            ids=[item["id"]]
        )

if __name__ == "__main__":
    ingest_faq()
