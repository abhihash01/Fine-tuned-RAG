import streamlit as st
from ingest import ingestor
from input_processor import input_processor
from prompt_conversatoin_chain import conversational_chain
import validators
class app:
    def run(self):
        ingest=ingestor()
        st.set_page_config("Fine tuned Rag applicaiton")
        st.header("RAG Applicaiton")


        with st.sidebar:
            st.title("Knowledge Bases")
            st.caption("No api required for enterprise models. Don't add both urls and pdfs together")
            model_temp= st.selectbox("Select Model", ("Gemini", "OpenAI","LLama","Mistral"))
            urls=pdf=None
            urls = st.text_input("URL", label_visibility="collapsed")
            pdfs= st.file_uploader("Upload PDFs",accept_multiple_files=True)
            if st.button("Store Knowledge"):
                with st.spinner("loading..."):
                    if pdfs:
                        try:
                            raw_text=ingest.extract_pdf_text(pdfs)
                            text_chunks = ingest.extract_text_chunks(raw_text)
                            ingest.store_vectors(text_chunks)
                        except Exception as e:
                            st.exception(f"Exception: {e}")
                    if urls:
                        if not validators.url(urls):
                            st.error("Please enter a valid url")
                        else:
                            #text_chunks = ingest.extract_url_text_chunks([urls])
                            #ingest.store_vectors_urls(text_chunks)

                            raw_text = ingest.extract_url_text([urls])
                            text_chunks = ingest.extract_text_chunks(raw_text)
                            ingest.store_vectors(text_chunks)


                    st.success("Done")
        
        question = st.text_input("Enter Question here")

        submit1 = st.button("Ask LLM")
        submit2 = st.button("Ask Knowledgebase")

        conver_chain = conversational_chain()
        
        inp_processor = input_processor()
        
        response = []
        if submit1:
            chat = conver_chain.load_chat()
            response = inp_processor.get_response(chat,question)
            st.write("Response: ", response.content)
        if submit2:
            chain = conver_chain.load_chain()
            docs = inp_processor.get_similar_docs(question)
            response = inp_processor.get_knowledge_response(chain,docs,question)
            st.write("Response: ", response["output_text"])


        
        return

if __name__=="__main__":
    application=app()
    application.run()
