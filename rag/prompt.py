# input_query = input('Ask me a question: ')
# retrieved_knowledge = retrieve(input_query)

# print('Retrieved knowledge:')
# for chunk, similarity in retrieved_knowledge:
#   print(f' - (similarity: {similarity:.2f}) {chunk}')

# instruction_prompt = f'''You are a helpful chatbot.
# Use only the following pieces of context to answer the question. Don't make up any new information:
# {'\n'.join([f' - {chunk}' for chunk, similarity in retrieved_knowledge])}
# '''

# stream = ollama.chat(
#   model=LANGUAGE_MODEL,
#   messages=[
#     {'role': 'system', 'content': instruction_prompt},
#     {'role': 'user', 'content': input_query},
#   ],
#   stream=True,
# )

# # print the response from the chatbot in real-time
# print('Chatbot response:')
# for chunk in stream:
#   print(chunk['message']['content'], end='', flush=True)

def generate_prompt(retrieved_knowledge, query):
    context = '\n'.join([f' - {chunk}' for chunk, similarity in retrieved_knowledge])
    return f'''You are a helpful chatbot.
Use only the following pieces of context to answer the question. Don't make up any new information:
{context}
'''