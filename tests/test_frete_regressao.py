import pytest
from frete import calcular_frete, calcular_total

# --- Regressão: casos herdados dos testes unitários ---
def test_regressao_frete_abaixo_do_limite():
    assert calcular_frete(249.99) == 15.0

def test_regressao_frete_no_limite_e_gratis():
    assert calcular_frete(250.0) == 0.0

# --- Regressão: casos herdados dos testes de integração ---
def test_regressao_total_com_frete_cobrado():
    assert calcular_total(100.0) == pytest.approx(115.0)

def test_regressao_total_com_frete_gratis():
    assert calcular_total(300.0) == pytest.approx(300.0)

# --- Regressão: caso herdado do teste funcional ---
def test_regressao_usuario_ve_total_correto_no_checkout():
    subtotal_do_carrinho = 50.0
    assert calcular_total(subtotal_do_carrinho) == pytest.approx(65.0)