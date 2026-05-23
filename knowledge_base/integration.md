# Integração de Aplicações e Mensageria na AWS

Serviços essenciais para desacoplamento de sistemas e arquiteturas orientadas a eventos.

---

### **1. Amazon SQS (Simple Queue Service)**
*   **Função:** Filas de mensagens para desacoplar componentes.
*   **Destaque:** Elimina a dependência direta entre sistemas (Assíncrono).
*   **Tipo FIFO:** Garante a ordem exata das mensagens e evita duplicidade.

### **2. Amazon SNS (Simple Notification Service)**
*   **Função:** Serviço de publicação/assinatura (Pub/Sub).
*   **Destaque:** Envio de mensagens para múltiplos assinantes simultaneamente (Fan-out).
*   **Exemplos:** Envio de e-mail, SMS ou gatilhos de Lambda.

### **3. Amazon EventBridge**
*   **Função:** Barramento de eventos serverless.
*   **Destaque:** Conecta aplicações usando dados de serviços AWS, aplicações próprias ou SaaS.
*   **Uso:** Roteamento de eventos com base em regras.

### **4. AWS Step Functions**
*   **Função:** Orquestrador de fluxos de trabalho (Workflows).
*   **Destaque:** Máquina de estados visual para coordenar múltiplos serviços AWS em sequências lógicas.
