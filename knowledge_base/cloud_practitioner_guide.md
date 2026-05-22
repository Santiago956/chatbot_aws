# Guia da Certificação AWS Cloud Practitioner (CLF-C02)

Este guia resume os pontos fundamentais para alunos iniciantes que desejam se preparar para a certificação de entrada da AWS.

## 1. O Exame em Resumo
- **Formato:** 65 questões (múltipla escolha ou múltipla resposta).
- **Duração:** 90 minutos.
- **Pontuação para Aprovação:** 700 de 1000.
- **Domínios:**
    - **Conceitos de Nuvem (24%):** Proposta de valor, economia e princípios de design.
    - **Segurança e Conformidade (30%):** Modelo de Responsabilidade Compartilhada e IAM.
    - **Tecnologia e Serviços (34%):** Serviços core e infraestrutura global.
    - **Faturamento, Preços e Suporte (12%):** Modelos de custo e planos de suporte.

## 2. Conceitos Fundamentais

### As 6 Vantagens da Nuvem
1.  **Troque despesas de capital por despesas variáveis:** Pague apenas pelo que consome.
2.  **Economias de escala massivas:** Preços menores devido ao grande volume de clientes da AWS.
3.  **Pare de adivinhar a capacidade:** Escale recursos conforme a demanda real.
4.  **Aumente a velocidade e agilidade:** Recursos disponíveis em minutos.
5.  **Pare de gastar com manutenção de Data Centers:** Foque no seu negócio, não na infraestrutura.
6.  **Torne-se global em minutos:** Implante em várias regiões com poucos cliques.

### Modelos de Implantação
- **Nuvem (Pública):** Tudo roda no provedor de nuvem.
- **Híbrida:** Conecta infraestrutura local (on-premises) com a nuvem.
- **On-premises (Nuvem Privada):** Recursos gerenciados localmente.

## 3. Segurança (Tópico Crítico)

### Modelo de Responsabilidade Compartilhada
- **AWS (Segurança DA Nuvem):** Hardware, infraestrutura global, camadas de rede física e instalações.
- **Cliente (Segurança NA Nuvem):** Dados, gerenciamento de identidades (IAM), configurações de firewall (Security Groups) e atualizações de sistemas operacionais (no caso do EC2).

## 4. Faturamento e Suporte

### Planos de Suporte AWS
| Plano | Foco | Custo | Resposta Crítica |
| :--- | :--- | :--- | :--- |
| **Basic** | Todos | Grátis | N/A (Apenas faturamento) |
| **Developer** | Testes | >$29/mês | < 12h (Sistema prejudicado) |
| **Business** | Produção | >$100/mês | < 1h (Sistema fora do ar) |
| **Enterprise** | Crítico | >$15k/mês | < 15 min (Crítico fora do ar) |

## 5. Tópicos Emergentes (CLF-C02)
- **IA e ML:** Amazon Bedrock e Amazon SageMaker.
- **Governança:** AWS Organizations e AWS Control Tower.
