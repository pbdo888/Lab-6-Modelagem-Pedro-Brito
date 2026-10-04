# Suíte de testes da TASK-01, escrita ANTES do código (TDD: fase Red).
# Cada teste traduz uma cláusula EARS de specs/checkout_frete.md em uma verificação automática.

# Importa as duas funções que ainda NÃO existem; na fase Red este import falha de propósito.
from frete import calcular_frete, calcular_total


# Conecta com: REQ-01 (Ubiquitous) -> abaixo do limite, a taxa de frete padrão é R$ 15,00.
def test_req01_taxa_padrao_abaixo_do_limite():
    # Subtotal de R$ 100,00 está abaixo de R$ 250,00, então deve cobrar a taxa padrão.
    assert calcular_frete(100.0) == 15.0


# Conecta com: REQ-01 (Ubiquitous) -> o total é o subtotal somado à taxa de frete.
def test_req01_total_soma_frete_ao_subtotal():
    # R$ 100,00 de produtos + R$ 15,00 de frete = R$ 115,00 no total.
    assert calcular_total(100.0) == 115.0


# Conecta com: REQ-01 (caso de fronteira) -> um centavo abaixo do limite ainda paga frete.
def test_req01_um_centavo_abaixo_do_limite_paga_frete():
    # R$ 249,99 ainda é "menor que R$ 250,00", então o frete padrão continua valendo.
    assert calcular_frete(249.99) == 15.0


# Conecta com: REQ-02 (IF/THEN) -> exatamente no limite (">= R$ 250,00") o frete é grátis.
def test_req02_frete_gratis_no_limite_exato():
    # O "maior OU IGUAL" da spec obriga a testar o valor exato da fronteira.
    assert calcular_frete(250.0) == 0.0


# Conecta com: REQ-02 (IF/THEN) -> acima do limite o frete também é grátis.
def test_req02_frete_gratis_acima_do_limite():
    # R$ 300,00 é maior que R$ 250,00, então a taxa deve ser zero.
    assert calcular_frete(300.0) == 0.0


# Conecta com: REQ-01 + REQ-02 -> com frete grátis, o total é igual ao próprio subtotal.
def test_req02_total_sem_frete_quando_gratis():
    # R$ 300,00 + R$ 0,00 de frete = R$ 300,00.
    assert calcular_total(300.0) == 300.0


# Conecta com: REQ-02 (mudança do Exercício 3) -> R$ 200,00, que antes era grátis, agora paga frete.
def test_req02_antigo_limite_de_200_agora_paga_frete():
    # Teste de regressão da regra antiga: garante que ninguém esqueceu o valor R$ 200,00 no código.
    assert calcular_frete(200.0) == 15.0
