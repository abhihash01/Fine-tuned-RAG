import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

class input_processor:
    def __init__(self) -> None:
        self.gemini_embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    def get_similar_docs(self,question,faiss_path="FAISS_store"):
        faiss_db = FAISS.load_local(faiss_path,self.gemini_embeddings)
        docs=faiss_db.similarity_search(question)
        return docs
    
    def get_response(self,chat,question):
        response = chat.invoke(question)
        return response
    
    def get_knowledge_response(self,chain,docs,question):
        response = chain({"input_documents":docs, "question":question})
        return response