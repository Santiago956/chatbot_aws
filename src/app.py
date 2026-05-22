import streamlit as st
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_core.prompts import PromptTemplate

# Carregar variáveis de ambiente se existirem
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

# Configuração da página
st.set_page_config(page_title="Assistente de Estudos AWS", page_icon="☁️", layout="wide")

st.title("☁️ Assistente de Estudos AWS")
st.markdown("""
### Bem-vindo ao seu Tutor Técnico Inteligente! 🚀
Este assistente foi desenvolvido para ajudar você a dominar os conceitos de **AWS Cloud** e se preparar para a certificação **Cloud Practitioner (CLF-C02)**.

**Como funciona?**
- **RAG (Retrieval-Augmented Generation):** O assistente não "inventa" respostas. Ele consulta a documentação oficial da AWS e whitepapers técnicos que estão na nossa base de conhecimento.
- **Transparência:** Todas as respostas vêm acompanhadas das fontes consultadas para que você possa validar e aprofundar seus estudos.
- **Privacidade e Performance:** Utilizamos embeddings locais (gratuitos) e a tecnologia da Groq Cloud para garantir respostas ultra-rápidas.

---
""")

# Barra lateral para configurações
with st.sidebar:
    st.header("Configurações")
    
    st.info("""
    **Guia Rápido:**
    1. Insira sua **Groq API Key** abaixo.
    2. Certifique-se de ter rodado `python src/ingestion.py` no terminal para processar os documentos.
    3. Digite sua dúvida sobre serviços AWS, segurança, custos ou arquitetura.
    """)
    
    groq_key = st.text_input("Groq API Key", type="password", value=os.getenv("GROQ_API_KEY", ""))
    
    if st.button("Limpar Histórico"):
        st.session_state.messages = []
        st.rerun()

# Inicializar histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir mensagens do histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def get_response(query, g_key):
    try:
        DB_PATH = "vectorstore/db_faiss"
        
        # Validar chave
        if not g_key:
            return "Por favor, insira sua Groq API Key na barra lateral.", []

        # Carregar base vetorial (Embeddings locais não precisam de chave)
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        if not os.path.exists(DB_PATH):
            return "Base de conhecimento não encontrada. Rode 'python src/ingestion.py' primeiro no terminal.", []
            
        vectorstore = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)
        
        # Template da Persona
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
        
        # Modelo Groq
        llm = ChatGroq(model_name="llama3-70b-8192", temperature=0, groq_api_key=g_key)
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=True,
            chain_type_kwargs={"prompt": PROMPT}
        )
        
        result = qa_chain.invoke({"query": query})
        return result["result"], result["source_documents"]
        
    except Exception as e:
        return f"Erro ao processar resposta: {str(e)}", []

# Campo de entrada do chat
if prompt := st.chat_input("Como posso ajudar nos seus estudos de AWS hoje?"):
    # Adicionar mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gerar resposta do assistente
    with st.chat_message("assistant"):
        with st.spinner("Consultando documentação AWS..."):
            response_text, sources = get_response(prompt, groq_key)
            
            st.markdown(response_text)
            
            if sources:
                with st.expander("Fontes Consultadas"):
                    for doc in sources:
                        st.write(f"- {doc.metadata['source']}")
    
    # Adicionar resposta ao histórico
    st.session_state.messages.append({"role": "assistant", "content": response_text})
