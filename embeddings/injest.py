import os
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

def load_data(data_folder):
    documents = []
    for subdir, _, files in os.walk(data_folder):
        for file in files:
            if file.endswith((".txt", ".md")):  # Add this check
                with open(os.path.join(subdir, file), 'r', encoding='utf-8') as f:
                    documents.append(f.read())
    return documents

def chunk_text(text, max_length=500):
    # Use newline-based splitting for markdown instead of period
    lines = text.split('\n')
    chunks, current = [], ""

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if len(current) + len(line) < max_length:
            current += line + " "
        else:
            chunks.append(current.strip())
            current = line + " "

    if current:
        chunks.append(current.strip())

    return chunks


def ingest_to_qdrant(collection_name="musicblocks_debugger"):
    qdrant = QdrantClient(host="localhost", port=6333)  # Use persistent DB via Docker
    model = SentenceTransformer("all-MiniLM-L6-v2")

    documents = load_data("data")
    all_chunks = []
    for doc in tqdm(documents):
        chunks = chunk_text(doc)
        all_chunks.extend(chunks)

    if not all_chunks:
        print("⚠️ No chunks created. Check if your .md/.txt files contain usable text.")
        return

    embeddings = model.encode(all_chunks).tolist()

    if not embeddings:
        print("⚠️ No data was embedded. Check if your `.md` files contain valid text.")
        return

    qdrant.recreate_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(size=len(embeddings[0]), distance=models.Distance.COSINE),
    )

    qdrant.upload_collection(
        collection_name=collection_name,
        vectors=embeddings,
        payload=[{"text": c} for c in all_chunks],
        ids=list(range(len(all_chunks)))
    )

    print(f"✅ Ingested {len(all_chunks)} chunks into Qdrant.")

if __name__ == "__main__":
    ingest_to_qdrant()
