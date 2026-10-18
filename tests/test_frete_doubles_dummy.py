# Test Double: DUMMY (Lab 8, Ex. 7.2 — arquivo de estudo: um papel por arquivo)
# Dummy = objeto que só existe para preencher um parâmetro obrigatório.
# A lógica nunca usa ele. Se usasse, o teste deveria quebrar.

from unittest.mock import Mock

import pytest

from frete import confirmar_frete


def test_dummy_usuario_so_preenche_a_assinatura():
    # Arrange
    usuario_dummy = object()  # objeto vazio: não tem nome, e-mail, nada
    logistica_stub = Mock()
    logistica_stub.consultar_taxa.return_value = 15.0
    notificacao = Mock()  # o código chama este serviço; aqui não conferimos nada nele

    # Act
    total = confirmar_frete("PED-1", 100.0, usuario_dummy, logistica_stub, notificacao)

    # Assert: funcionou sem tocar no usuário.
    # Se o código fizesse "usuario.nome", o object() daria AttributeError e o teste quebraria.
    assert total == 115.0


# Prova de que é dummy: qualquer valor serve, e o resultado não muda.
@pytest.mark.parametrize("usuario_dummy", [None, object(), "qualquer coisa"])
def test_dummy_qualquer_valor_serve_porque_nao_e_usado(usuario_dummy):
    # Arrange
    logistica_stub = Mock()
    logistica_stub.consultar_taxa.return_value = 15.0

    # Act
    total = confirmar_frete("PED-2", 100.0, usuario_dummy, logistica_stub, Mock())

    # Assert
    assert total == 115.0
