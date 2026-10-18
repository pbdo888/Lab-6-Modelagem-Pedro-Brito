#Testes de integração Para verificar se as funções calcular frete e calcular total estão conversando
import pytest

from frete import calcular_frete, calcular_total

#Verificar total com subtotal>250 (frete grátis: 300 + 0)
def test_verificar_total_acima_do_limite():
    assert calcular_total(300.0)==pytest.approx(300.0)

#Verificar total com subtotal=250 NO LIMITE (frete grátis: 250 + 0)
def test_verificar_total_no_limite():
    assert calcular_total(250.0)==pytest.approx(250.0)

#Verificar total com subtotal 1 centavo abaixo (paga frete: 249,99 + 15)
def test_verificar_total_um_centavo_abaixo():
    assert calcular_total(249.99)==pytest.approx(264.99)


# Verificar total com subtotal<LIMITE_FRETE_GRATIS (paga frete: 200 + 15)
def test_verificar_total_abaixo_do_limite():
    assert calcular_total(200.0)==pytest.approx(215.0)
