import pytest
from rag.prompt import generate_prompt

def test_generate_prompt():
    retrieved_knowledge = [("Yellowglow", 0.95), ("Yellow Radiance", 0.80)]
    query = "Can you give me the name of a yellow glowing plant?"
    expected_output = """You are a helpful chatbot.
Use only the following pieces of context to answer the question. Don't make up any new information:
 - Yellowglow
 - Yellow Radiance
"""
    
    assert generate_prompt(retrieved_knowledge, query) == expected_output
