# Serviços Core da AWS

Visão geral dos serviços fundamentais para construção de infraestrutura na AWS.

---

### **Amazon EC2 (Elastic Compute Cloud)**

**Informações Gerais**
O Amazon EC2 fornece capacidade de computação segura e redimensionável na nuvem. Ele oferece controle total sobre os recursos de computação e permite a execução em um ambiente comprovado da Amazon.

**Casos de Uso**
*   **Aplicações Empresariais:** Execução de servidores web, servidores de aplicação e bancos de dados.
*   **Computação de Alto Desempenho (HPC):** Processamento de cargas de trabalho intensivas.
*   **Desenvolvimento macOS:** Criação e teste de cargas de trabalho macOS sob demanda.
*   **Machine Learning:** Infraestrutura otimizada para treinamento e implantação de ML.

**Principais Características**
*   **Escalabilidade Elástica:** Ajuste de capacidade via *Auto Scaling*.
*   **Variedade de Instâncias:** Mais de 1000 tipos otimizados (CPU, Memória, Armazenamento).
*   **Segurança Nitro:** Isolamento e proteção baseados em hardware.
*   **Modelos de Preço:** On-Demand, Spot (até 90% desc.), e Savings Plans.

---

### **Amazon S3 (Simple Storage Service)**

**Informações Gerais**
Serviço de armazenamento de objetos com escalabilidade, disponibilidade de dados, segurança e performance líderes do setor.

**Casos de Uso**
*   **Data Lakes:** Base para análise de dados e IA.
*   **Backup e Disaster Recovery:** Armazenamento durável e em conformidade.
*   **Aplicações Cloud-Native:** Armazenamento de mídia, logs e configurações.
*   **Arquivamento:** Baixo custo com classes *S3 Glacier*.

**Principais Características**
*   **Durabilidade Extrema:** Projetado para 99,999999999% (11 noves).
*   **Classes de Armazenamento:** Otimização via *S3 Intelligent-Tiering*.
*   **Segurança:** Criptografia padrão e controles de acesso robustos.
*   **Performance IA:** Latência de milissegundos com *S3 Express One Zone*.

---

### **AWS IAM (Identity and Access Management)**

**Informações Gerais**
Gerenciamento seguro de acesso aos serviços e recursos da AWS. Permite criar usuários, grupos e funções com permissões específicas.

**Casos de Uso**
*   **Controle de Acesso Granular:** Definir quem acessa o quê e sob quais condições.
*   **Identidades de Carga de Trabalho:** Permissões seguras para aplicações (ex: EC2 acessando S3).
*   **Governança Multi-conta:** Controle centralizado via *IAM Identity Center*.
*   **Menor Privilégio:** Ajuste contínuo para garantir apenas o acesso necessário.

**Principais Características**
*   **Credenciais Temporárias:** Uso de funções (roles) em vez de chaves fixas.
*   **Políticas ABAC:** Permissões baseadas em atributos (tags).
*   **Analisador de Acesso:** Validação de políticas e identificação de acessos externos.

---

### **Amazon VPC (Virtual Private Cloud)**

**Informações Gerais**
Provisionamento de uma seção logicamente isolada da nuvem AWS para lançar recursos em uma rede virtual definida pelo usuário.

**Casos de Uso**
*   **Aplicações Multi-camadas:** Isolar web servers (público) de bancos de dados (privado).
*   **Conectividade Híbrida:** Conexão com rede local via VPN ou *Direct Connect*.
*   **Extensão de Data Center:** Nuvem como extensão segura da infraestrutura local.

**Principais Características**
*   **Isolamento Lógico:** Controle total de IP, sub-redes e tabelas de rotas.
*   **Segurança de Rede:** Security Groups e NACLs.
*   **Conectividade Privada:** *VPC Peering* e *Transit Gateway*.
