import chromadb
from core.embeddings import embed

client = chromadb.PersistentClient(path="db/chroma")
collection = client.get_or_create_collection("poetry")

def add_poem(id, text, metadata=None):

    emb = get_embedding(text)

    collection.add(
        ids=[str(id)],
        embeddings=[emb],
        documents=[text],
        metadatas=[metadata or {}]
    )


def search_similar(text, k=5):

    emb = get_embedding(text)

    results = collection.query(
        query_embeddings=[emb],
        n_results=k
    )

    return results
