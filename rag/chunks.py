from rag.embeddings import generate_embedding

# Each element in the VECTOR_DB will be a tuple (chunk, embedding)
VECTOR_DB = []

def add_chunk_to_database(chunk):
    embedding = generate_embedding(chunk)
    VECTOR_DB.append((chunk, embedding))

def get_vector_db():
    return VECTOR_DB