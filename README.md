# Retrieval-Augmented Generation (RAG) Project

This project implements a Retrieval-Augmented Generation (RAG) pipeline to answer user queries by combining document retrieval with a language model's generative capabilities.


## Steps of Retrieval Augmented Generation
1. **Ingestion of documents**  
   Loading and preprocessing documents to feed the model knowledge.

2. **Chunking**  
   Splitting texts into smaller, manageable chunks.

3. **Embeddings**  
   Converting chunks into vector representations using an embedding model.

4. **Vector storage**  
   Saving these chunks and their embeddings in a vector database.

5. **User query**  
   Accepting a question from the user.

6. **Database search**  
   Searching for chunks most relevant to the question using similarity metrics.

7. **LLM's answer**  
   Reformulating the retrieved chunks to generate a coherent and accurate response.

---

## Steps of this project

### 1. Virtual Environment Creation
To avoid compatibility issues between packages, create a virtual environment in Python:

```bash
$ python3 -m venv ragvenv
$ source ragvenv/bin/activate
```

### 2. Install Dependencies
Install the required tools and models:

```bash
sudo snap install ollama
ollama pull hf.co/CompendiumLabs/bge-base-en-v1.5-gguf
ollama pull hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF
```

Use Poetry to manage dependencies:

```bash
poetry init
poetry add ollama
```


### 3. Dataset Loading
The dataset is loaded from a text file using the [`load_dataset`](rag/dataset_loader.py) function:

```python
from rag.dataset_loader import load_dataset

dataset = load_dataset('rag/data/fruit-trees.txt')
```

### 4. Chunking and Embedding
The dataset is split into chunks, and each chunk is converted into a vector representation using the [`add_chunk_to_database`](rag/chunks.py) function:

```python
from rag.chunks import add_chunk_to_database

for chunk in dataset:
    add_chunk_to_database(chunk)
```

### 5. Query Retrieval
When a user asks a question, the system retrieves the most relevant chunks from the vector database using the [`retrieve`](rag/retrieval.py) function:

```python
from rag.retrieval import retrieve

retrieved_knowledge = retrieve(input_query)
```

### 6. Prompt Generation
The retrieved chunks are formatted into a prompt for the language model using the [`generate_prompt`](rag/prompt.py) function:

```python
from rag.prompt import generate_prompt

instruction_prompt = generate_prompt(retrieved_knowledge, input_query)
```

### 7. Language Model Interaction
The language model generates a response based on the prompt and user query using the [`chat_with_llm`](rag/llm.py) function:

```python
from rag.llm import chat_with_llm

response = chat_with_llm(instruction_prompt, input_query)
```

### 8. Running the Application
The entire pipeline is orchestrated in [`app.py`](app.py). Run the application with:

```bash
python app.py
```

## Project architecture
.
├── app.py
├── poetry.lock
├── pyproject.toml
├── rag
│   ├── chunks.py
│   ├── data
│   │   └── fruit-trees.txt
│   ├── dataset_loader.py
│   ├── embeddings.py
│   ├── __init.__py
│   ├── llm.py
│   ├── prompt.py
│   ├── retrieval.py
│   └── vectors.py
└── README.md


## REFERENCES
- [Hugging Face Blog: Make Your Own RAG](https://huggingface.co/blog/ngxson/make-your-own-rag)