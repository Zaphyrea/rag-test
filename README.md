

## Steps of Retrieval Augmented Generation
1. Ingestion of documents
Loading and preprocessing documents which will feed the model knowledge.

2. Chunking
Separating texts in smaller bits 

3. Embeddings
Converting chunks into vectors

4. Vector's storage
Saving these chunks in a database

5. User query
Questioning the model about a specific subject

6. Database search
Searching for chunks closer to the question

7. Llm's answer
Reformating these chunks to generate a correct answer.


## Steps of this project

### First version
1. Virtual environment creation
To avoid problem compatibility between packages of different projects, it's necessary to create a venv in python.

``` bash
$ python3 -m venv ragvenv
$ source ragvenv/bin/activate
```


``` bash
sudo snap install ollama
 ollama pull hf.co/CompendiumLabs/bge-base-en-v1.5-gguf
ollama pull hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF
```

## packages installation
```bash
poetry init
```
I chose to use poetry rather than pip because it's managing conflicts between packages automatically
poetry add ollama




## REFERENCES

https://huggingface.co/blog/ngxson/make-your-own-rag 