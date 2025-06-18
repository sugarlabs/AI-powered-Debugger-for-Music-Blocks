from qdrant_client import QdrantClient
from dotenv import load_dotenv
import os

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

def retrieve_relevant_chunks(query, top_k=5, collection_name="mb_docs"):
    from sentence_transformers import SentenceTransformer
    qdrant = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY
    )
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_vector = model.encode(query).tolist()

    search_result = qdrant.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=top_k
    )

    return [hit.payload.get("text", "") for hit in search_result if "text" in hit.payload]
