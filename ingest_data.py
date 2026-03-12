from app.ingest import load_documents
from app.chunking import split_documents
from app.pinecone_store import create_pinecone_index

print("Loading documents...")

docs = load_documents()

print("Splitting into chunks...")

chunks = split_documents(docs)

print("Example chunks:")
print("Chunk 1:", chunks[0])
print("Chunk 2:", chunks[1])

create_pinecone_index(chunks)

print("Ingestion complete")
print("Total pages:", len(docs))
print("Total chunks:", len(chunks))