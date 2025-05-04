import pytest
from rag.embeddings import generate_embedding

def test_generate_embedding():
    text = "Test text for embedding."
    embedding = generate_embedding(text)
    assert isinstance(embedding, list), "Embedding should be a list"
    assert len(embedding) > 0, "Embedding should not be empty"