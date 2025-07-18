import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

st.set_page_config(page_title="Interner Firmen-Chatbot")
st.title("💬 Firmen-Chatbot mit Dokumentenwissen")

query = st.text_input("Frag mich etwas zu unseren Dokumenten:")

# Vektor-DB laden
db = Chroma(persist_directory="data/", embedding_function=OpenAIEmbeddings())
retriever = db.as_retriever(search_kwargs={"k": 3})

qa = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    retriever=retriever,
    return_source_documents=True
)

if query:
    result = qa(query)
    st.write("### Antwort:")
    st.write(result['result'])

    st.write("### Quellen:")
    for doc in result['source_documents']:
        st.write(f"- {doc.metadata.get('source', 'Unbekannt')}")
