#Testes de integração Para verificar se as funções calcular frete e calcular total estão conversando
from frete import calcular_frete, calcular_total

#Verificar total com subtotal>250
def test_verificar_total01():
    assert calcular_total(300.0)==pytest.approx(315.0)

#Verificar total com subtotal=250 NO LIMITE
def test_verificar_total02():
    assert calcular_total(250.0)==pytest.approx(250.0)

#Verificar total com subtotal 1 centavo abaixo
def test_verificar_total():
    assert calcular_total(249.99)==pytest.approx(249.99)


# Verificar total com subtotal<LIMITE_FRETE_GRATIS
def test_verificar_total():
    assert calcular_total(200.0)==pytest.approx(200)

