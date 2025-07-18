import os
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader, UnstructuredExcelLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

docs = []
directory = "docs"

for file in os.listdir(directory):
    path = os.path.join(directory, file)
    if file.endswith(".pdf"):
        loader = PyPDFLoader(path)
    elif file.endswith(".docx"):
        loader = Docx2txtLoader(path)
    elif file.endswith(".xlsx"):
        loader = UnstructuredExcelLoader(path)
    else:
        continue
    loaded = loader.load()
    for doc in loaded:
        doc.metadata["source"] = file
    docs.extend(loaded)

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

db = Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory="data/")
db.persist()

print("Dokumente erfolgreich eingelesen und indiziert.")
