# Módulo de cálculo de frete do checkout.
# Fonte da verdade: specs/checkout_frete.md (cláusulas REQ-01 a REQ-05).
# Constituição, item 3: toda função cita a cláusula REQ-xx que a justifica.
#   TASK-01 (Lab 6): REQ-01 e REQ-02
#   TASK-02 (Lab 8, Ex. 7.2): REQ-03 e REQ-04
#   TASK-03 (Lab 8, Ex. 7.4, TDD): REQ-05

# REQ-01 e REQ-02: taxa de frete padrão e limite do frete grátis.
# Ficam num dicionário (simula uma tabela de configuração no banco de dados)
# para que os testes possam trocá-los temporariamente com patch.dict (Stub).
dicio_taxa_limite = {"taxa_frete": 15.0, "limite": 250.0}

# REQ-05: regiões com taxa adicional e o limite próprio de frete grátis delas.
REGIOES_COM_ADICIONAL = {"Norte", "Nordeste"}
TAXA_ADICIONAL_REGIAO = 10.0
LIMITE_FRETE_GRATIS_REGIAO = 300.0


# Retorna apenas a taxa de frete para um subtotal (e, opcionalmente, a região de entrega).
def calcular_frete(subtotal, regiao=None):
    # REQ-05 (IF/THEN): Norte/Nordeste vem primeiro, porque muda o limite do frete grátis.
    if regiao in REGIOES_COM_ADICIONAL:
        # "superior a R$ 300,00" -> maior que (>): exatamente R$ 300,00 ainda paga.
        if subtotal > LIMITE_FRETE_GRATIS_REGIAO:
            return 0.0
        # Taxa padrão (R$ 15,00) + adicional da região (R$ 10,00) = R$ 25,00.
        return dicio_taxa_limite["taxa_frete"] + TAXA_ADICIONAL_REGIAO

    # REQ-02 (IF/THEN): "maior ou igual a R$ 250,00" -> (>=): exatamente R$ 250,00 já é grátis.
    if subtotal >= dicio_taxa_limite["limite"]:
        return 0.0

    # REQ-01 (Ubiquitous): em qualquer outro caso, aplica a taxa padrão.
    return dicio_taxa_limite["taxa_frete"]


# Retorna o valor total do pedido (subtotal + frete).
def calcular_total(subtotal, regiao=None):
    # REQ-01: o total é o subtotal somado à taxa de frete (que já considera REQ-02 e REQ-05).
    return subtotal + calcular_frete(subtotal, regiao)


# ---------- Serviços externos (REQ-03 e REQ-04) ----------
# No laboratório esses serviços não existem de verdade. Os métodos lançam erro de
# propósito: se algum teste usar o serviço real em vez de um Test Double, ele quebra
# na hora, o que garante que os testes estão isolados.

class ServicoLogisticaAPI:
    # REQ-03: consulta a taxa de frete local na transportadora.
    def consultar_taxa(self, subtotal):
        # Na vida real faria uma chamada de rede para a transportadora.
        raise NotImplementedError("Chamada de rede real")


class ServicoNotificacao:
    # REQ-04: envia ao cliente o alerta de envio com o rastreio do pedido.
    def enviar_notificacao_rastreio(self, pedido_id):
        # Na vida real mandaria e-mail/SMS para o cliente.
        raise NotImplementedError("Envio real de notificação")


# Confirma o frete de um pedido e devolve o total a pagar.
# "usuario" é a sessão do usuário logado: faz parte da assinatura exigida pelo
# checkout, mas não participa do cálculo (no teste ele é preenchido por um Dummy).
def confirmar_frete(pedido_id, subtotal, usuario, servico_logistica, servico_notificacao):
    # REQ-02: a partir do limite o frete é grátis, sem precisar consultar a transportadora.
    if subtotal >= dicio_taxa_limite["limite"]:
        frete = 0.0
    else:
        # REQ-03: a taxa local vem do serviço externo de logística.
        frete = servico_logistica.consultar_taxa(subtotal)

    # REQ-04: depois de confirmar o frete, avisa o cliente (1 vez, com o ID do pedido).
    servico_notificacao.enviar_notificacao_rastreio(pedido_id)

    return subtotal + frete
