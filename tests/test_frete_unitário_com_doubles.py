# Exercício 7.2 (Lab 8) — Teste unitário isolado com Test Doubles (unittest.mock).
# Função testada: confirmar_frete (REQ-03 e REQ-04 em specs/checkout_frete.md).
# Nenhuma chamada de rede real: os dois serviços externos são substituídos por doubles.
#   Dummy -> preenche o parâmetro "usuario", que a lógica nunca usa
#   Stub  -> ServicoLogisticaAPI devolve uma taxa fixa programada (REQ-03)
#   Mock  -> ServicoNotificacao é fiscalizado: 1 chamada, com o ID certo (REQ-04)

from unittest.mock import Mock

from frete import confirmar_frete


def test_confirmar_frete_com_test_doubles():
    # Arrange
    # DUMMY: preenche o parâmetro "usuario", mas a lógica nunca usa
    usuario_dummy = object()

    # STUB: API de logística devolve taxa fixa, sem chamada de rede (REQ-03)
    logistica_stub = Mock()
    logistica_stub.consultar_taxa.return_value = 22.0

    # MOCK: serviço de notificação que vamos fiscalizar (REQ-04)
    notificacao_mock = Mock()

    # Act
    total = confirmar_frete(
        pedido_id="PED-123",
        subtotal=100.0,  # abaixo de R$ 250,00, para a API de logística ser consultada
        usuario=usuario_dummy,
        servico_logistica=logistica_stub,
        servico_notificacao=notificacao_mock,
    )

    # Assert
    # usa a taxa do stub (22), não a padrão (15): prova que o stub foi usado
    assert total == 122.0
    # MOCK: chamado exatamente 1 vez, com o ID correto do pedido
    notificacao_mock.enviar_notificacao_rastreio.assert_called_once_with("PED-123")
