import pytest
from frete import calcular_total

# Teste funcional: usuário finaliza compra com carrinho pequeno
def test_usuario_ve_frete_cobrado_no_checkout():
    subtotal_do_carrinho = 50.0
    total_exibido = calcular_total(subtotal_do_carrinho)
    assert total_exibido == pytest.approx(65.0)

# Teste funcional: usuário finaliza compra com carrinho grande
def test_usuario_ve_frete_gratis_no_checkout():
    subtotal_do_carrinho = 300.0
    total_exibido = calcular_total(subtotal_do_carrinho)
    assert total_exibido == pytest.approx(300.0)