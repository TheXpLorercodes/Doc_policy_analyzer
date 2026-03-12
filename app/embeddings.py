from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(text):

    embedding = model.encode(text)

    return embedding.tolist()