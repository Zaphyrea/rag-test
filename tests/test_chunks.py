import pytest
from rag.chunks import add_chunk_to_database, get_vector_db

def test_add_chunk_to_database():
    chunk = "This is a test chunk."
    add_chunk_to_database(chunk)
    vector_db = get_vector_db()
    assert len(vector_db) == 1, "Vector DB should contain one entry"
    assert vector_db[0][0] == chunk, "Chunk should match the input"