# Test Doubles: MOCK e SPY (Lab 8, Ex. 7.2 — arquivo de estudo: um papel por arquivo)
# Mock = substituto que FISCALIZA as chamadas: foi chamado? quantas vezes? com o quê?
# Spy  = "espião": deixa o código REAL rodar e só anota as chamadas para conferir depois.

from unittest.mock import Mock, patch

import frete
from frete import calcular_total, confirmar_frete


# MOCK (o pedido no Ex. 7.2): depois de confirmar o frete, a notificação de rastreio
# é enviada exatamente 1 vez, com o ID correto do pedido (REQ-04).
def test_mock_notificacao_enviada_uma_vez_com_id_do_pedido():
    # Arrange
    logistica_stub = Mock()
    logistica_stub.consultar_taxa.return_value = 15.0
    notificacao_mock = Mock()

    # Act
    confirmar_frete("PED-777", 100.0, None, logistica_stub, notificacao_mock)

    # Assert: a pergunta agora é "como foi chamado?", e não "qual o resultado?"
    notificacao_mock.enviar_notificacao_rastreio.assert_called_once_with("PED-777")


# MOCK: mesmo com frete grátis (REQ-02), o cliente continua sendo avisado (REQ-04).
def test_mock_notificacao_enviada_mesmo_com_frete_gratis():
    # Arrange
    notificacao_mock = Mock()

    # Act
    confirmar_frete("PED-778", 300.0, None, Mock(), notificacao_mock)

    # Assert
    notificacao_mock.enviar_notificacao_rastreio.assert_called_once_with("PED-778")


# MOCK: com frete grátis (REQ-02/REQ-03) a transportadora nem é consultada.
# O MESMO tipo de objeto (Mock) que é stub em outros testes aqui é mock,
# porque quem define o papel é o USO: neste teste conferimos a chamada.
def test_mock_logistica_nao_e_consultada_quando_frete_e_gratis():
    # Arrange
    logistica_mock = Mock()

    # Act
    confirmar_frete("PED-779", 300.0, None, logistica_mock, Mock())

    # Assert
    logistica_mock.consultar_taxa.assert_not_called()


# SPY: calcular_total usa o calcular_frete REAL, e o espião confere como ele foi chamado.
def test_spy_calcular_total_chama_o_calcular_frete_real():
    # Arrange: "wraps=" faz o espião repassar cada chamada para a função verdadeira
    with patch("frete.calcular_frete", wraps=frete.calcular_frete) as espiao:
        # Act
        total = calcular_total(100.0, "Nordeste")

    # Assert 1: o resultado é o REAL (a regra de verdade rodou: 100 + 25)
    assert total == 125.0
    # Assert 2: e o espião anotou a chamada, com os argumentos certos
    espiao.assert_called_once_with(100.0, "Nordeste")
