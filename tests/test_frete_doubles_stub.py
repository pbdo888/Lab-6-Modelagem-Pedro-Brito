# Test Double: STUB (Lab 8, Ex. 7.2 — arquivo de estudo: um papel por arquivo)
# Stub = substituto que devolve respostas FIXAS, programadas por nós.
# Ele controla a ENTRADA do código; o teste confere o RESULTADO (não as chamadas).

from unittest.mock import Mock, patch

from frete import calcular_frete, confirmar_frete

# Valores DIFERENTES dos reais (15 e 250) de propósito: com os mesmos valores,
# o teste passaria até sem o stub e não provaria nada.
CONFIG_FALSA = {"taxa_frete": 20.0, "limite": 100.0}


# Stub 1: a "tabela de configuração" (dicionário) trocada com patch.dict.
def test_stub_da_configuracao_cobra_a_taxa_programada():
    # Arrange: o stub vale só dentro do "with"; depois o dicionário volta ao original
    with patch.dict("frete.dicio_taxa_limite", CONFIG_FALSA):
        # Act
        frete = calcular_frete(50.0)

    # Assert: taxa do stub (20), não a real (15)
    assert frete == 20.0


def test_stub_da_configuracao_usa_o_limite_programado():
    # Arrange
    with patch.dict("frete.dicio_taxa_limite", CONFIG_FALSA):
        # Act
        frete = calcular_frete(100.0)

    # Assert: pelo limite real (250) pagaria 15; pelo limite do stub (100) é grátis
    assert frete == 0.0


# Stub 2 (o pedido no Ex. 7.2): ServicoLogisticaAPI devolve uma taxa fixa, sem rede.
def test_stub_servico_logistica_devolve_taxa_fixa():
    # Arrange
    logistica_stub = Mock()
    logistica_stub.consultar_taxa.return_value = 30.0  # resposta programada

    # Act
    total = confirmar_frete("PED-10", 100.0, None, logistica_stub, Mock())

    # Assert: só olhamos o RESULTADO; conferir chamadas seria papel de mock
    assert total == 130.0
