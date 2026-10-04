# Especificação: Checkout — Cálculo de Frete

> **Fonte Única da Verdade (SSOT).** Esta spec descreve O QUE o sistema deve fazer,
> usando a notação **EARS** (Easy Approach to Requirements Syntax). Testes e código
> derivam daqui; se houver divergência, quem está errado é o código.
>
> Padrões EARS usados:
> - **Ubiquitous** (sempre vale): `THE SYSTEM SHALL <ação>`
> - **IF/THEN** (comportamento condicional/indesejado): `IF <condição>, THEN THE SYSTEM SHALL <ação>`

## Requisitos

**REQ-01 (Ubiquitous):** THE SYSTEM SHALL calcular o valor total adicionando a taxa
de frete padrão de R$ 15,00 ao subtotal do carrinho.

**REQ-02 (IF/THEN):** IF o subtotal do carrinho for maior ou igual a R$ 200,00,
THEN THE SYSTEM SHALL conceder frete grátis (taxa = R$ 0,00).

## Fora de escopo

- Cupons de desconto, regiões de entrega e validação de valores inválidos
  **não** fazem parte desta spec. Qualquer código nesse sentido é *drift*.
