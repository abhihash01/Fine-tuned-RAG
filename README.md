# Fine-tuned-RAG

## Test App Online

The app has been deployed online on streamlit cloud [here](https://fine-tuned-rag-jmg7bkiqykdc7mpsdaguqw.streamlit.app/)

To use the knowledge base functionality, upload documents and process first to run queries on them.  

  

## To Run the application

  

  

git clone https://github.com/abhihash01/Fine-tuned-RAG.git

pip install -r requirements.txt

  

### Add api key in the .env file

streamlit run app.py

  

  

## Retrieval Augmented Generation

  

  

### The application presently uses Google Gemini API for response. The application has 2 options. It can either query the llm or query the knowledge base. The knowledgebase presently supports multiple files, but only of the pdf types.

  

  

### To query the Knowledgebase, the knowledge base has to be created first by uploading the pdf documents and processing it. To query the llm model, the direct Ask LLM function can be used.

  

  

## To Do
* support other knowledge sources - weblink
* support other knowledge sources - image
* support history conversations for knowledgebase query
* support history conversations for LLM
* extend LLM offereing to Opnai
* extend LLM offering to opensource- LLama2, Mistral 7*8B...
* extend embedding offereing to Instructor embeddings, Huggingface embeddings, Bert Embeddings, Sentence Transformers etc
* Add part to extend existant vectorstore with new information
* add vectordb, chromadb, pinecone to handle huge data
* Integrate the Fine tuned application