# ☁️ Assistente de Estudos AWS (RAG + Groq + Streamlit)

Este projeto é um **Assistente de Estudos Inteligente** especializado em AWS Cloud e preparação para a certificação **Cloud Practitioner (CLF-C02)**. Ele utiliza a técnica de **RAG (Retrieval-Augmented Generation)** para responder perguntas baseando-se exclusivamente em documentação oficial da AWS.

## 🚀 Tecnologias Utilizadas

- **IA de Chat:** [Groq Cloud](https://groq.com/) (Llama 3 70B) para inferência ultra-rápida.
- **Embeddings:** HuggingFace (all-MiniLM-L6-v2) - **Execução Local e Gratuita**.
- **Orquestração:** LangChain.
- **Banco de Dados Vetorial:** FAISS (Local).
- **Interface:** Streamlit.
- **Processamento de Dados:** PyPDF e Markdown.

## 📂 Estrutura do Projeto

- `docs/`: Fontes originais em PDF (Well-Architected, Guia de Exame, etc).
- `knowledge_base/`: Documentação processada em Markdown para melhor leitura da IA.
- `src/ingestion.py`: Script para processar documentos e criar a base vetorial.
- `src/chatbot.py`: Interface de chat via terminal (CLI).
- `src/app.py`: Interface visual moderna com Streamlit.
- `requirements.txt`: Dependências do sistema.
- `.env.example`: Modelo para configuração de chaves de API.

## 🛠️ Configuração e Instalação

### 1. Pré-requisitos
- Python 3.9 ou superior.
- Espaço em disco: ~700MB (para dependências e ambiente virtual).

### 2. Instalação
Clone o repositório e instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Configuração de Segurança
Copie o arquivo de exemplo e insira suas chaves de API da **OpenAI** e **Groq**:
```bash
cp .env.example .env
```
Edite o arquivo `.env` e preencha os valores:
```env
OPENAI_API_KEY=sua_chave_openai
GROQ_API_KEY=sua_chave_groq
```

## 📖 Como Usar

### Passo 1: Ingestão de Dados
Antes de conversar, você precisa processar os documentos para criar a inteligência local:
```bash
python src/ingestion.py
```
*Isso criará a pasta `vectorstore/` com seus dados processados.*

### Passo 2: Iniciar o Assistente
Você tem duas opções para interagir:

**Opção A: Interface Web (Recomendado)**
Oferece uma experiência de chat fluida com histórico e exibição de fontes.
```bash
streamlit run src/app.py
```

**Opção B: Terminal (CLI)**
Para interações rápidas via linha de comando.
```bash
python src/chatbot.py
```

## 🔒 Segurança e Boas Práticas
- O projeto utiliza um arquivo `.gitignore` para garantir que suas chaves de API e dados locais não sejam commitados.
- Todas as respostas incluem **referências textuais às fontes**, conforme as diretrizes do `GEMINI.md`.

---
*Este projeto foi desenvolvido como material de apoio para o curso de AWS Cloud e Engenharia de Dados.*
