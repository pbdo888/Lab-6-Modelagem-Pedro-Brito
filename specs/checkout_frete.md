# Especificação: Checkout — Cálculo de Frete

> **Fonte Única da Verdade (SSOT).** Esta spec descreve O QUE o sistema deve fazer,
> usando a notação **EARS** (Easy Approach to Requirements Syntax). Testes e código
> derivam daqui; se houver divergência, quem está errado é o código.
>
> Padrões EARS usados:
> - **Ubiquitous** (sempre vale): `THE SYSTEM SHALL <ação>`
> - **Event-driven** (quando um evento acontece): `WHEN <evento>, THE SYSTEM SHALL <ação>`
> - **IF/THEN** (comportamento condicional/indesejado): `IF <condição>, THEN THE SYSTEM SHALL <ação>`

## Requisitos

**REQ-01 (Ubiquitous):** THE SYSTEM SHALL calcular o valor total adicionando a taxa
de frete padrão de R$ 15,00 ao subtotal do carrinho.

**REQ-02 (IF/THEN):** IF o subtotal do carrinho for maior ou igual a R$ 250,00,
THEN THE SYSTEM SHALL conceder frete grátis (taxa = R$ 0,00).

**REQ-03 (Event-driven):** WHEN o frete de um pedido for confirmado com subtotal
inferior a R$ 250,00, THE SYSTEM SHALL consultar a taxa de frete local no serviço
externo de logística (`ServicoLogisticaAPI`) e somá-la ao subtotal.
Com subtotal maior ou igual a R$ 250,00 vale a REQ-02: frete grátis, sem consultar o serviço.

**REQ-04 (Event-driven):** WHEN o frete de um pedido for confirmado, THE SYSTEM SHALL
enviar exatamente uma notificação de rastreio, com o ID do pedido, pelo serviço de
notificações (`ServicoNotificacao`).

**REQ-05 (IF/THEN):** IF a região de entrega for "Norte" ou "Nordeste", THEN THE SYSTEM
SHALL cobrar a taxa de frete padrão (R$ 15,00) acrescida de uma taxa adicional de
R$ 10,00, exceto quando o subtotal do carrinho for superior a R$ 300,00, caso em que o
frete é grátis (R$ 0,00).

> **Interpretação adotada para a REQ-05** (o enunciado não diz o que acontece entre
> R$ 250,00 e R$ 300,00): para Norte e Nordeste, o limite de frete grátis da REQ-02
> (R$ 250,00) é substituído pelo limite de R$ 300,00, **exclusivo** ("superior a" → `>`).
>
> | Região | Subtotal | Frete |
> |---|---|---|
> | Norte / Nordeste | R$ 100,00 | R$ 25,00 |
> | Norte / Nordeste | R$ 280,00 | R$ 25,00 |
> | Norte / Nordeste | R$ 300,00 | R$ 25,00 |
> | Norte / Nordeste | R$ 300,01 | R$ 0,00 |
> | Outras regiões ou não informada | segue REQ-01 e REQ-02 | |

## Histórico de mudanças (documentação viva)

| Data | Cláusula | Mudança | Motivo |
|---|---|---|---|
| 2026-10-04 | REQ-02 | Limite do frete grátis: R$ 200,00 → R$ 250,00 | Decisão do Product Owner (Exercício 3) |
| 2026-10-18 | REQ-03, REQ-04 | Confirmação do frete passa a depender dos serviços de logística e de notificações | Lab 8, Exercício 7.2 (TASK-02) |
| 2026-10-18 | REQ-05 | Taxa adicional de R$ 10,00 para Norte e Nordeste | Lab 8, Exercício 7.4 (TASK-03, TDD) |

## Fora de escopo

- Cupons de desconto e validação de valores inválidos (subtotal zero ou negativo)
  **não** fazem parte desta spec. Qualquer código nesse sentido é *drift*.
- Regiões além de Norte e Nordeste não têm regra própria (seguem REQ-01 e REQ-02).
- Normalização do nome da região (maiúsculas/minúsculas, acentos, espaços).
- Tratamento de falhas dos serviços externos (timeout, erro de rede).
