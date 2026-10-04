# Módulo de cálculo de frete do checkout (TASK-01).
# Implementação MÍNIMA: só o necessário para os testes de tests/test_frete.py passarem.
# Fonte da verdade: specs/checkout_frete.md (cláusulas REQ-01 e REQ-02).

# REQ-01: taxa de frete padrão de R$ 15,00 (constante nomeada evita "número mágico" no código).
TAXA_FRETE_PADRAO = 15.0
# REQ-02: a partir deste subtotal (inclusive) o frete é grátis (alterado de 200 para 250 na spec).
LIMITE_FRETE_GRATIS = 250.0


# Retorna apenas a taxa de frete para um dado subtotal do carrinho.
def calcular_frete(subtotal):
    # REQ-02 (IF/THEN): IF subtotal >= R$ 250,00 THEN taxa = R$ 0,00 ("maior ou igual" -> ">=").
    if subtotal >= LIMITE_FRETE_GRATIS:
        # Frete grátis: devolve zero como float para manter o mesmo tipo da taxa padrão.
        return 0.0
    # REQ-01 (Ubiquitous): em qualquer outro caso, aplica a taxa padrão.
    return TAXA_FRETE_PADRAO


# Retorna o valor total do pedido (subtotal + frete).
def calcular_total(subtotal):
    # REQ-01: o total é o subtotal somado à taxa de frete (que já considera a REQ-02).
    return subtotal + calcular_frete(subtotal)
