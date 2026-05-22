# Pilar de Segurança - AWS Well-Architected Framework

O Pilar de Segurança foca na proteção de informações e sistemas.

### 1. Princípios de Design (Conceitos Fundamentais)
*   **Implementar uma base de identidade forte:** Centralize o gerenciamento de identidades e aplique o princípio do privilégio mínimo.
*   **Manter a rastreabilidade:** Monitore, alerte e audite ações e alterações no ambiente em tempo real.
*   **Aplicar segurança em todas as camadas:** Utilize múltiplos controles (rede, instâncias, aplicações) para uma defesa em profundidade.
*   **Automatizar as melhores práticas de segurança:** Crie arquiteturas seguras e escaláveis através de automação baseada em código.
*   **Proteger dados em repouso e em trânsito:** Utilize criptografia, tokenização e controle de acesso.
*   **Manter as pessoas afastadas dos dados:** Reduza o acesso direto ou manual para diminuir riscos de erro ou manipulação.
*   **Preparar-se para incidentes:** Desenvolva processos de resposta a incidentes e realize simulações regularmente.

### 2. Áreas de Foco e Melhores Práticas

#### Gerenciamento de Identidade e Acesso (IAM)
*   **Identidades:** Use mecanismos de autenticação fortes (MFA) e credenciais temporárias.
*   **Permissões:** Defina guardrails organizacionais e analise acessos públicos ou entre contas.

#### Detecção
*   **Monitoramento:** Configure logs de serviços e aplicações em locais padronizados.
*   **Resposta:** Correlacione alertas e inicie remediações automáticas para recursos não conformes.

#### Proteção de Infraestrutura
*   **Rede:** Crie camadas de rede e controle o fluxo de tráfego entre elas.
*   **Computação:** Realize gerenciamento de vulnerabilidades e utilize imagens endurecidas (hardened).

#### Proteção de Dados
*   **Classificação:** Entenda e automatize a identificação da sensibilidade dos dados.
*   **Criptografia:** Aplique gerenciamento seguro de chaves e certificados para dados em repouso e em trânsito.

#### Resposta a Incidentes
*   **Preparação:** Desenvolva planos de gerenciamento e playbooks de resposta.
*   **Operação:** Pré-implante ferramentas e estabeleça um framework de aprendizado pós-incidente.

#### Segurança de Aplicações
*   **Ciclo de Vida:** Automatize testes de segurança no pipeline de release e realize revisões de código e testes de penetração regulares.
