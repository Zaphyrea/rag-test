import pytest
from rag.llm import chat_with_llm

def test_chat_with_llm():
    prompt = "This is a test prompt."
    query = "What is this?"
    response = chat_with_llm(prompt, query)
    assert response is not None, "Response should not be None"