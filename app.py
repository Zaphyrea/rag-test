from rag.dataset_loader import load_dataset
from rag.chunks import add_chunk_to_database
from rag.retrieval import retrieve
from rag.prompt import generate_prompt
from rag.llm import chat_with_llm

# Load the dataset
dataset = load_dataset('rag/data/plants.txt')

# Add chunks to the database
for i, chunk in enumerate(dataset):
    add_chunk_to_database(chunk)
    print(f'Added chunk {i+1}/{len(dataset)} to the database')

# Chatbot
input_query = input('Ask me a question: ')
retrieved_knowledge = retrieve(input_query)

print('Retrieved knowledge:')
for chunk, similarity in retrieved_knowledge:
    print(f' - (similarity: {similarity:.2f}) {chunk}')

instruction_prompt = generate_prompt(retrieved_knowledge, input_query)

print('Chatbot response:')
for chunk in chat_with_llm(instruction_prompt, input_query):
    print(chunk['message']['content'], end='', flush=True)