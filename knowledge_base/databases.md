# Bancos de Dados Relacionais na AWS

Bancos de dados relacionais (SQL) são fundamentais para aplicações que exigem consistência transacional e relacionamentos complexos entre dados.

---

### **1. Amazon RDS (Relational Database Service)**

**Visão Geral**
Serviço gerenciado que facilita a configuração, operação e escalabilidade de bancos de dados relacionais na nuvem. A AWS gerencia tarefas de administração pesadas, como patches de software, backups e hardware.

**Motores Suportados**
*   MySQL, PostgreSQL, MariaDB, Oracle, SQL Server e IBM DB2.

**Alta Disponibilidade (Multi-AZ)**
*   Cria uma réplica síncrona em uma Zona de Disponibilidade (AZ) diferente.
*   Em caso de falha da instância principal, a AWS altera automaticamente o DNS para a instância standby (failover automático).

---

### **2. Amazon Aurora**

**Visão Geral**
Banco de dados relacional construído para a nuvem, totalmente gerenciado e compatível com MySQL e PostgreSQL.

**Diferenciais Técnicos**
*   **Performance:** Até 5x mais rápido que MySQL padrão e 3x mais que PostgreSQL padrão.
*   **Durabilidade:** Armazena 6 cópias dos dados em 3 AZs diferentes por padrão.
*   **Escalabilidade:** Suporta até 15 réplicas de leitura com latência mínima.
*   **Auto-scaling de Armazenamento:** Aumenta automaticamente até 256 TiB.

**Aurora Serverless**
*   Escala automaticamente a capacidade de computação (ACUs) com base na demanda da aplicação. Ideal para cargas de trabalho intermitentes ou imprevisíveis.

---

### **3. Comparação RDS vs. Aurora**

| Recurso | Amazon RDS | Amazon Aurora |
| :--- | :--- | :--- |
| **Réplicas de Leitura** | Até 5 | Até 15 |
| **Failover** | 60-120 segundos | < 30 segundos |
| **Armazenamento** | Provisionado (EBS) | Auto-scaling (Distribuído) |
| **Replicação de Dados** | Baseada em instâncias | 6 cópias em 3 AZs (Nível de armazenamento) |

---

### **4. O que saber para a Prova (Cloud Practitioner)**

*   **Managed vs. Unmanaged:** Saiba que no RDS a AWS cuida do SO e do hardware, mas você ainda é responsável pelas configurações do banco e otimização de queries.
*   **Amazon RDS:** É a escolha para compatibilidade total com bancos tradicionais.
*   **Amazon Aurora:** É a escolha para alta performance e escalabilidade massiva.
*   **Shared Responsibility:** A AWS cuida da segurança **da** infraestrutura; você cuida da segurança **dos** dados e usuários.
*   **Diferença SQL vs. NoSQL:** RDS/Aurora são SQL (Estruturados). DynamoDB é NoSQL (Chave-Valor).
