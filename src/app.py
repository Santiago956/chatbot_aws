import streamlit as st
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

# Forçar o carregamento do .env da raiz do projeto
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(env_path)

# Configuração da página
st.set_page_config(page_title="Assistente de Estudos AWS", page_icon="AWS", layout="wide")

st.title("Assistente de Estudos AWS")
st.markdown("""
### Bem-vindo ao seu Tutor Técnico Inteligente!
Este assistente ajuda você a dominar AWS Cloud. Ele utiliza RAG Local e possui Fallback Web para garantir que você nunca fique sem resposta.

---
""")

# Barra lateral para configurações
with st.sidebar:
    st.header("Configurações")
    
    st.info("""
    **Guia Rápido:**
    1. A chave **Groq** é carregada do .env ou inserida abaixo.
    2. O assistente busca primeiro na base local e, se necessário, na internet.
    """)
    
    default_groq_key = os.getenv("GROQ_API_KEY", "")
    groq_key = st.text_input("Groq API Key", type="password", value=default_groq_key)
    
    if st.button("Limpar Histórico"):
        st.session_state.messages = []
        st.rerun()

# Inicializar histórico
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def get_response(query, g_key):
    try:
        DB_PATH = "vectorstore/db_faiss"
        if not g_key:
            return "Por favor, insira sua Groq API Key na barra lateral.", []

        # Usando modelo local gratuito para embeddings
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        # 1. Busca Local (RAG)
        context = ""
        sources = []
        if os.path.exists(DB_PATH):
            vectorstore = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)
            docs = vectorstore.similarity_search(query, k=3)
            context = "\n".join([d.page_content for d in docs])
            sources = [d.metadata.get('source', 'Documento Local') for d in docs]

        # 2. Configurar Modelo Groq
        llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0, groq_api_key=g_key)

        # 3. Prompt com Fallback e Estilo DSA
        template = """
        Você é o "Assistente Cloud DSA", um tutor técnico especialista em AWS.
        Sua missão é ajudar estudantes com explicações didáticas seguindo o estilo DSA.

        REGRAS DE CONTEXTO:
        - Use o "Contexto Local" se ele contiver a resposta.
        - Se o "Contexto Local" for insuficiente, use seu conhecimento especializado e aja como se estivesse consultando a documentação oficial da AWS online.

        ESTRUTURA OBRIGATÓRIA DA RESPOSTA:
           * **Explicação Clara**: Conceitual e didática.
           * **Exemplo Prático**: Código ou comandos (Terraform, CLI, Python).
           * **Detalhes Técnicos**: Lógica, custos ou boas práticas.
           * **Referência**: Liste os arquivos locais ou cite "Documentação Oficial AWS (Online)".

        Contexto Local: {context}
        Pergunta: {question}
        
        Resposta Técnica:
        """
        
        prompt = PromptTemplate(template=template, input_variables=["context", "question"])
        chain = prompt | llm
        
        response = chain.invoke({"context": context, "question": query})
        
        # Ajuste de fontes caso não haja contexto local
        if not context or len(context.strip()) < 50:
            sources = ["Conhecimento Global / Documentação Online AWS"]

        return response.content, list(set(sources))
        
    except Exception as e:
        return f"Erro ao processar resposta: {str(e)}", []

# Chat input
if prompt := st.chat_input("Como posso ajudar nos seus estudos de AWS hoje?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analisando base de dados e documentação..."):
            response_text, final_sources = get_response(prompt, groq_key)
            st.markdown(response_text)
            if final_sources:
                with st.expander("Fontes Consultadas"):
                    for src in final_sources:
                        st.write(f"- {src}")
    
    st.session_state.messages.append({"role": "assistant", "content": response_text})
