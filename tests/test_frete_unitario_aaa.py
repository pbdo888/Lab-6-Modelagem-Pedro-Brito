# Exercício 7.1 (Lab 8) — Teste unitário com o padrão AAA (Arrange, Act, Assert).
# Cenário: REQ-01 (frete padrão de R$ 15,00 abaixo de R$ 250,00) e
#          REQ-02 (frete grátis, R$ 0,00, para R$ 250,00 ou mais).
# Fonte da verdade: specs/checkout_frete.md
#
# AAA "estritamente": cada teste tem as 3 fases separadas e nesta ordem,
# com UMA única ação (Act) por teste.
#   Arrange -> prepara os dados de entrada e o resultado esperado
#   Act     -> executa a função testada (uma vez só)
#   Assert  -> confere se o resultado é o esperado

from frete import calcular_frete


# REQ-01: um valor bem abaixo do limite paga a taxa padrão.
def test_aaa_frete_padrao_para_carrinho_abaixo_de_250():
    # Arrange
    subtotal = 100.0
    frete_esperado = 15.0

    # Act
    frete = calcular_frete(subtotal)

    # Assert
    assert frete == frete_esperado


# REQ-01 (fronteira): um centavo abaixo do limite ainda paga a taxa padrão.
def test_aaa_frete_padrao_um_centavo_abaixo_do_limite():
    # Arrange
    subtotal = 249.99
    frete_esperado = 15.0

    # Act
    frete = calcular_frete(subtotal)

    # Assert
    assert frete == frete_esperado


# REQ-02 (fronteira): exatamente R$ 250,00 já tem frete grátis ("maior ou IGUAL").
def test_aaa_frete_gratis_no_limite_exato_de_250():
    # Arrange
    subtotal = 250.0
    frete_esperado = 0.0

    # Act
    frete = calcular_frete(subtotal)

    # Assert
    assert frete == frete_esperado


# REQ-02: um centavo acima do limite também tem frete grátis.
def test_aaa_frete_gratis_acima_de_250():
    # Arrange
    subtotal = 250.01
    frete_esperado = 0.0

    # Act
    frete = calcular_frete(subtotal)

    # Assert
    assert frete == frete_esperado
