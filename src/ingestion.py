import os
from dotenv import load_dotenv

# Forçar o carregamento do .env da raiz do projeto
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def ingest_docs():
    # Caminhos
    KB_PATH = "knowledge_base/"
    DOCS_PATH = "docs/"
    DB_PATH = "vectorstore/db_faiss"

    print("--- Carregando documentos ---")
    
    # Carregar Markdowns da Knowledge Base
    md_loader = DirectoryLoader(KB_PATH, glob="*.md", loader_cls=TextLoader, loader_kwargs={'encoding': 'utf-8'})
    md_docs = md_loader.load()
    
    # Carregar PDFs da pasta docs
    pdf_loader = DirectoryLoader(DOCS_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
    pdf_docs = pdf_loader.load()
    
    all_docs = md_docs + pdf_docs
    print(f"Total de documentos carregados: {len(all_docs)}")

    # Dividir texto em chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    documents = text_splitter.split_documents(all_docs)
    print(f"Total de chunks criados: {len(documents)}")

    # Criar Embeddings e Vector Store (Local e Gratuito)
    print("--- Criando Base Vetorial (HuggingFace Local) ---")
    
    # Modelo leve e eficiente para embeddings locais: all-MiniLM-L6-v2
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(documents, embeddings)
    
    # Salvar localmente
    vectorstore.save_local(DB_PATH)
    print(f"Base vetorial salva em: {DB_PATH}")

if __name__ == "__main__":
    ingest_docs()
