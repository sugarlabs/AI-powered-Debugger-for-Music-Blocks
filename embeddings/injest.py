import os
import config
from langchain_community.embeddings import HuggingFaceEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# Setup
client = QdrantClient(
    url=config.QDRANT_URL,
    api_key=config.QDRANT_API_KEY
)

docs_dir = "data/guide"
raw_docs = []

# Read text files
for filename in os.listdir(docs_dir):
    if filename.endswith(".txt") or filename.endswith(".md"):
        filepath = os.path.join(docs_dir, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    raw_docs.append(Document(page_content=content, metadata={"source": filename}))
        except Exception as e:
            print(f"Error reading {filename}: {e}")

if not raw_docs:
    raise ValueError("No valid documents found in the 'docs/' directory.")

# Split documents into smaller chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=30)
chunked_docs = splitter.split_documents(raw_docs)

# Generate embeddings
embedding_model = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)
texts = [doc.page_content for doc in chunked_docs]
embeddings = embedding_model.embed_documents(texts)

# Create collection if needed
collection_name = "mb_docs"
existing_collections = client.get_collections().collections
collection_names = [c.name for c in existing_collections]

if collection_name not in collection_names:
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=len(embeddings[0]), distance=Distance.COSINE)
    )
    print(f"✅ Created collection '{collection_name}' in Qdrant.")
else:
    print(f"Collection '{collection_name}' already exists. Skipping creation.")

# Prepare and upload points
points = [
    PointStruct(
        id=i,
        vector=embeddings[i],
        payload={
            "page_content": chunked_docs[i].page_content,
            **chunked_docs[i].metadata
        }
    )
    for i in range(len(chunked_docs))
]

client.upsert(collection_name=collection_name, points=points)
print(f"✅ Uploaded {len(points)} chunks to Qdrant collection '{collection_name}'.")
