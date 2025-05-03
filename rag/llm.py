import ollama

LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'


def chat_with_llm(prompt, query):
    stream = ollama.chat(
        model=LANGUAGE_MODEL,
        messages=[
            {'role': 'system', 'content': prompt},
            {'role': 'user', 'content': query},
        ],
        stream=True,
    )
    return stream

