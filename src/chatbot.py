import os
from dotenv import load_dotenv

# Forçar o carregamento do .env da raiz do projeto
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_core.prompts import PromptTemplate

def get_chatbot_response(query):
    DB_PATH = "vectorstore/db_faiss"
    
    groq_key = os.getenv("GROQ_API_KEY")

    if not groq_key:
        return {"result": "Erro: Chave de API GROQ não configurada no .env.", "source_documents": []}

    # Carregar base vetorial com Embeddings Locais (Gratuitos)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    if not os.path.exists(DB_PATH):
        return {"result": "Erro: Base de conhecimento não encontrada. Rode 'python src/ingestion.py' primeiro.", "source_documents": []}
        
    vectorstore = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)
    
    # Configurar o modelo Groq (Persona e regras do GEMINI.md)
    template = """
    Você é um Assistente de Estudos especializado em AWS.
    Responda à pergunta do usuário APENAS com base no contexto fornecido abaixo.
    Se a informação não estiver no contexto, diga: "Não encontrei informação suficiente na base de conhecimento para responder com segurança."
    
    REGRA CRÍTICA: TODA resposta deve conter obrigatoriamente links ou referências textuais claras indicando a origem da informação (ex: nome do arquivo ou link).

    Contexto: {context}
    Pergunta: {question}
    
    Resposta Técnica:
    """
    
    PROMPT = PromptTemplate(template=template, input_variables=["context", "question"])
    
    # Utilizando Llama 3.3 via Groq para alta performance (sucessor do Llama 3)
    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0,
        groq_api_key=groq_key
    )
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )
    
    result = qa_chain.invoke({"query": query})
    return result

if __name__ == "__main__":
    user_query = input("Pergunte algo sobre AWS: ")
    response = get_chatbot_response(user_query)
    
    print("\n--- RESPOSTA ---")
    print(response["result"])
    
    print("\n--- FONTES CONSULTADAS ---")
    for doc in response["source_documents"]:
        print(f"- {doc.metadata['source']}")
