from pinecone import Pinecone
import os
from dotenv import load_dotenv
from app.embeddings import get_embeddings

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")
host = os.getenv("HOST")

pc = Pinecone(api_key=api_key)
index = pc.Index(host=host)


def create_pinecone_index(chunks):

    vectors = []

    for i, chunk in enumerate(chunks):

        embedding = get_embeddings(chunk.page_content)

        vectors.append({
            "id": f"chunk_{i}",
            "values": embedding,
            "metadata": {
                "text": chunk.page_content,
                "page": chunk.metadata.get("page"),
                "source": chunk.metadata.get("source")
            }
        })

    index.upsert(vectors=vectors)
    print(f"Uploaded {len(vectors)} vectors to Pinecone")


def search_query(query):

    query_embedding = get_embeddings(query)

    results = index.query(
        vector=query_embedding,
        top_k=5,
        include_metadata=True
    )

    context = ""

    print("\nRetrieved Matches:\n")

    for match in results["matches"]:

        score = match["score"]
        text = match["metadata"]["text"]
        page = match["metadata"]["page"]
        source = match["metadata"]["source"]

        print(f"Score: {score}")

        context += f"""
Source: {source}
Page: {page + 1}

{text}

"""

    return context