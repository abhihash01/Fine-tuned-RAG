import streamlit as st
from ingest import ingestor
from input_processor import input_processor
from prompt_conversatoin_chain import conversational_chain
class app:
    def run(self):
        ingest=ingestor()
        st.set_page_config("Fine tuned Rag applicaiton")
        st.header("RAG Applicaiton")


        with st.sidebar:
            st.title("Knowledge Bases")
            pdfs= st.file_uploader("Upload PDFs",accept_multiple_files=True)
            if st.button("Store Knowledge"):
                with st.spinner("loading..."):
                    raw_text=ingest.extract_pdf_text(pdfs)
                    text_chunks = ingest.extract_text_chunks(raw_text)
                    ingestor.store_vectors(text_chunks)
                    st.success("Done")
        
        question = st.text_input("Enter Question here")

        submit1 = st.button("Ask LLM")
        submit2 = st.button("Ask Knowledgebase")

        conver_chain = conversational_chain()
        chain = conver_chain.load_chain()
        inp_processor = input_processor()
        docs = inp_processor.get_similar_docs(question)

        if submit1:
            response = inp_processor.get_response(chain,question)
        if submit2:
            response = inp_processor.get_knowledge_response(chain,docs,question)

        st.write("Response: ", response["output_text"])






        
        return

if __name__=="__main__":
    application=app()
    application.run()
