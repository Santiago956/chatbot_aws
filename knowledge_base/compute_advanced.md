# Computação Serverless e Containers na AWS

Detalhes sobre os serviços modernos de execução de código e orquestração de containers.

---

### **1. AWS Lambda (Serverless)**

**Descrição**
Serviço de computação orientado a eventos que permite executar código sem gerenciar servidores. Você paga apenas pelo tempo de computação consumido.

**Características**
*   **Gatilhos:** S3, DynamoDB, Kinesis, API Gateway, SQS.
*   **Linguagens:** Python, Node.js, Java, Go, Ruby, .NET.
*   **Escalabilidade:** Escala automaticamente em resposta a eventos recebidos.

**Caso de Uso**
*   Processamento de imagens enviadas ao S3.
*   Backends de APIs simples.
*   Tarefas programadas (CRON).

---

### **2. Containers na AWS (ECS e EKS)**

#### **Amazon ECS (Elastic Container Service)**
*   **O que é:** Orquestrador de containers nativo da AWS. Muito integrado com serviços AWS (IAM, VPC, CloudWatch).
*   **Vantagem:** Simplicidade e baixo custo operacional.

#### **Amazon EKS (Elastic Kubernetes Service)**
*   **O que é:** Serviço gerenciado do Kubernetes. Mantém compatibilidade total com a ferramenta aberta original.
*   **Vantagem:** Portabilidade entre nuvens e ambientes locais.

---

### **3. AWS Fargate (Serverless para Containers)**

**Descrição**
Motor de computação para containers que elimina a necessidade de gerenciar instâncias EC2 subjacentes. Funciona tanto com ECS quanto com EKS.

**Vantagem**
*   Elimina a gestão de infraestrutura de clusters.
*   Isolamento de segurança no nível de tarefa.
*   Paga apenas pelo que o container utiliza (CPU/Memória).

---

### **4. AWS Batch**
*   Serviço focado em processamento em lote em grande escala, otimizando o uso de recursos de computação conforme a carga de trabalho.
