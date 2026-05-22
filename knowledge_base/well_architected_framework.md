# AWS Well-Architected Framework

O AWS Well-Architected Framework ajuda a entender os prós e contras das decisões tomadas ao construir sistemas na AWS. Ele fornece uma abordagem consistente para avaliar arquiteturas e implementar designs escaláveis.

## Princípios de Design Gerais
O framework recomenda seis princípios gerais para o design de arquitetura na nuvem:

1.  **Interromper a adivinhação de capacidade:** Elimine a necessidade de prever a demanda para evitar recursos ociosos ou falta de capacidade. Use o escalonamento automático para ajustar a capacidade conforme necessário.
2.  **Testar sistemas em escala de produção:** Na nuvem, você pode criar um ambiente duplicado em escala total, testar e depois desativar os recursos, pagando apenas pelo tempo de uso.
3.  **Automatizar para facilitar a experimentação arquitetônica:** A automação permite criar e replicar sistemas com baixo custo e esforço, facilitando alterações e rastreamento.
4.  **Permitir arquiteturas evolutivas:** Em ambientes tradicionais, decisões de arquitetura costumam ser estáticas. Na nuvem, você pode evoluir sua arquitetura conforme as necessidades do negócio mudam.
5.  **Impulsionar arquiteturas usando dados:** Colete dados sobre como suas escolhas arquitetônicas afetam o desempenho e o custo para tomar decisões informadas.
6.  **Melhorar através de "Game Days":** Simule eventos de falha ou picos de tráfego em produção para entender onde o sistema pode ser melhorado e como a equipe responde.

---

## Os 6 Pilares do Framework

### 1. Excelência Operacional (Operational Excellence)
Foca na execução e monitoramento de sistemas para entregar valor de negócio e na melhoria contínua de processos e procedimentos.
*   **Temas principais:** Automatizar alterações, responder a eventos e definir padrões para gerenciar operações diárias.

### 2. Segurança (Security)
Foca na proteção de informações, sistemas e ativos, aproveitando as tecnologias de nuvem para melhorar a postura de segurança.
*   **Temas principais:** Gerenciamento de identidade e acesso, detecção de ameaças, proteção de infraestrutura e proteção de dados.

### 3. Confiabilidade (Reliability)
Garante que uma carga de trabalho execute sua função pretendida de forma correta e consistente quando esperado.
*   **Temas principais:** Design de sistemas distribuídos, planejamento de recuperação de desastres e como lidar com mudanças na demanda.

### 4. Eficiência de Performance (Performance Efficiency)
Foca no uso eficiente de recursos de computação para atender aos requisitos do sistema e na manutenção dessa eficiência à medida que a tecnologia evolui.
*   **Temas principais:** Seleção de tipos de recursos otimizados, monitoramento de performance e tomada de decisões baseadas em dados.

### 5. Otimização de Custos (Cost Optimization)
Foca em evitar gastos desnecessários e garantir que todos os recursos entreguem o máximo valor pelo menor preço.
*   **Temas principais:** Entendimento de gastos ao longo do tempo, controle de alocação de fundos e escolha de modelos de preços adequados.

### 6. Sustentabilidade (Sustainability)
Foca na minimização do impacto ambiental da execução de cargas de trabalho na nuvem.
*   **Temas principais:** Entendimento do impacto, maximização da utilização de recursos e redução de recursos necessários para cada carga de trabalho.
