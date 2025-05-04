import pytest
from rag.retrieval import retrieve
from rag.chunks import add_chunk_to_database

def test_retrieve():
    add_chunk_to_database("This is a test chunk.")
    query = "test"
    results = retrieve(query)
    assert len(results) > 0, "Retrieve should return at least one result"
    assert "test" in results[0][0], "Result should contain the query term"