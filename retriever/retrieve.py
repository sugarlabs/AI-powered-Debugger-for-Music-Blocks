from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

def retrieve_relevant_chunks(query, top_k=5, collection_name="musicblocks_debugger"):
    qdrant = QdrantClient(host="localhost", port=6333)  # Use host="localhost" for persistent DB
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_vector = model.encode(query).tolist()

    search_result = qdrant.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=top_k
    )

    return [hit.payload["text"] for hit in search_result]
