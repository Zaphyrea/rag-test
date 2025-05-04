def generate_prompt(retrieved_knowledge, query):
    context = '\n'.join([f' - {chunk}' for chunk, similarity in retrieved_knowledge])
    return f'''You are a helpful chatbot.
Use only the following pieces of context to answer the question. Don't make up any new information:
{context}
'''