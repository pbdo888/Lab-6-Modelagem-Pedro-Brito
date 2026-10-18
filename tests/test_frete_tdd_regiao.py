# Exercício 7.4 (Lab 8) — TDD da nova regra de negócio REQ-05 (Norte/Nordeste).
# Fonte da verdade: specs/checkout_frete.md (REQ-05) | Task: tasks/TASK-03.md
#
# Ciclo TDD seguido:
#   1. Red      -> este arquivo foi escrito ANTES do código; o pytest falhou com
#                  "TypeError: calcular_frete() takes 1 positional argument but 2 were given".
#   2. Green    -> src/frete.py ganhou o mínimo para todos os testes passarem.
#   3. Refactor -> o código foi limpo (constantes com nome, um bloco por tipo de região)
#                  e os testes continuaram verdes.
#
# Regra: Norte/Nordeste pagam a taxa padrão (R$ 15,00) + R$ 10,00 de adicional,
# exceto se o subtotal for SUPERIOR a R$ 300,00 (aí o frete é grátis).
# "superior a" -> maior que (>): exatamente R$ 300,00 ainda paga.

import pytest

from frete import calcular_frete, calcular_total


# O primeiro teste do ciclo (o que nasceu vermelho): Norte e Nordeste pagam o adicional.
@pytest.mark.parametrize("regiao", ["Norte", "Nordeste"])
def test_req05_norte_e_nordeste_pagam_taxa_padrao_mais_adicional(regiao):
    # Arrange
    subtotal = 100.0
    frete_esperado = 25.0  # 15 (padrão) + 10 (adicional)

    # Act
    frete = calcular_frete(subtotal, regiao)

    # Assert
    assert frete == frete_esperado


# Fronteira do "superior a R$ 300,00": exatamente R$ 300,00 ainda paga.
@pytest.mark.parametrize("regiao", ["Norte", "Nordeste"])
def test_req05_exatamente_300_ainda_paga_adicional(regiao):
    # Arrange
    subtotal = 300.0
    frete_esperado = 25.0

    # Act
    frete = calcular_frete(subtotal, regiao)

    # Assert
    assert frete == frete_esperado


# Um centavo acima de R$ 300,00: frete grátis.
@pytest.mark.parametrize("regiao", ["Norte", "Nordeste"])
def test_req05_acima_de_300_frete_gratis(regiao):
    # Arrange
    subtotal = 300.01
    frete_esperado = 0.0

    # Act
    frete = calcular_frete(subtotal, regiao)

    # Assert
    assert frete == frete_esperado


# Interpretação registrada na spec: entre R$ 250,00 e R$ 300,00, Norte/Nordeste ainda pagam.
@pytest.mark.parametrize("subtotal", [250.0, 280.0])
def test_req05_entre_250_e_300_vale_o_limite_da_regiao(subtotal):
    # Arrange
    regiao = "Nordeste"
    frete_esperado = 25.0

    # Act
    frete = calcular_frete(subtotal, regiao)

    # Assert
    assert frete == frete_esperado


# As outras regiões não mudam: REQ-01 e REQ-02 continuam valendo.
@pytest.mark.parametrize(
    "regiao, subtotal, frete_esperado",
    [
        ("Sudeste", 100.0, 15.0),
        ("Sul", 249.99, 15.0),
        ("Centro-Oeste", 250.0, 0.0),
        (None, 100.0, 15.0),  # sem região: comportamento antigo
    ],
)
def test_req05_outras_regioes_seguem_req01_e_req02(regiao, subtotal, frete_esperado):
    # Arrange: os dados vêm do parametrize acima

    # Act
    frete = calcular_frete(subtotal, regiao)

    # Assert
    assert frete == frete_esperado


# O total do pedido também usa a regra nova.
def test_req05_total_do_pedido_no_nordeste():
    # Arrange
    subtotal = 100.0
    total_esperado = 125.0  # 100 + 25

    # Act
    total = calcular_total(subtotal, "Nordeste")

    # Assert
    assert total == total_esperado
