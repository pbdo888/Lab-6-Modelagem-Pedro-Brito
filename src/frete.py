# Módulo de cálculo de frete do checkout (TASK-01).
# Implementação MÍNIMA: só o necessário para os testes de tests/test_frete.py passarem.
# Fonte da verdade: specs/checkout_frete.md (cláusulas REQ-01 e REQ-02).

# REQ-01: taxa de frete padrão de R$ 15,00 (constante nomeada evita "número mágico" no código).
TAXA_FRETE_PADRAO = 15.0
# REQ-02: a partir deste subtotal (inclusive) o frete é grátis.
LIMITE_FRETE_GRATIS = 200.0


# Retorna apenas a taxa de frete para um dado subtotal do carrinho.
def calcular_frete(subtotal):
    # REQ-02 (IF/THEN): IF subtotal >= R$ 200,00 THEN taxa = R$ 0,00 ("maior ou igual" -> ">=").
    if subtotal >= LIMITE_FRETE_GRATIS:
        # Frete grátis: devolve zero como float para manter o mesmo tipo da taxa padrão.
        return 0.0
    # REQ-01 (Ubiquitous): em qualquer outro caso, aplica a taxa padrão.
    return TAXA_FRETE_PADRAO


# Retorna o valor total do pedido (subtotal + frete).
def calcular_total(subtotal):
    # REQ-01: o total é o subtotal somado à taxa de frete (que já considera a REQ-02).
    return subtotal + calcular_frete(subtotal)


# ==== CÓDIGO GERADO PELA IA A PARTIR DO PROMPT AMBÍGUO (EXERCÍCIO 2) ====
# Prompt: "Implemente a funcionalidade de aplicação de cupom de desconto 'DESCONTO10' para a classe de frete."
# ATENÇÃO: nada abaixo tem cláusula EARS na spec -> isto é DRIFT / sobre-implementação de propósito.
import json  # [DRIFT] import no meio do arquivo, só para persistência não pedida
CUPONS = {"DESCONTO10": 0.10, "FRETE20": 0.20, "BLACKFRIDAY": 0.50}  # [DRIFT] cupons extras inventados
def aplicar_cupom(subtotal, cupom, cpf_cliente=None):  # [DRIFT] função sem REQ correspondente
    print("aplicando cupom", cupom, "para cpf", cpf_cliente)  # [DRIFT][SEGURANÇA] log sem padrão vazando dado sensível
    for codigo in CUPONS:  # [DRIFT][PERFORMANCE] loop desnecessário: bastava CUPONS.get(cupom)
        if codigo == cupom:  # compara cada chave com o cupom recebido
            frete = calcular_frete(subtotal)  # recalcula o frete normal
            total = (subtotal + frete) * (1 - CUPONS[codigo])  # [DRIFT] desconto aplicado também no frete (ambíguo)
            with open("cupons_usados.json", "a") as f:  # [DRIFT] persistência em disco não solicitada
                f.write(json.dumps({"cupom": cupom, "cpf": cpf_cliente}))  # [SEGURANÇA] grava CPF em texto puro
            return total  # devolve o total com desconto
    return calcular_total(subtotal)  # [SEGURANÇA] cupom inválido é ignorado silenciosamente (sem validação)
