# TASK-03 — Taxa adicional para Norte e Nordeste (Lab 8, Ex. 7.4 — TDD)

> **Task atômica:** uma unidade de trabalho pequena o bastante para o agente de IA
> executar de uma vez, sem precisar ver o projeto inteiro.

## Contexto fornecido ao agente (isolamento estrito)

Forneça ao agente **apenas**:
- `constitution.md`
- `specs/checkout_frete.md`
- este arquivo (`tasks/TASK-03.md`)

## Escopo (tamanho mínimo)

- Cobre **apenas** a REQ-05 em `calcular_frete` e `calcular_total`.
- O parâmetro `regiao` é opcional (`regiao=None`): quem chama sem região continua com o
  comportamento antigo, então os testes dos Labs 6 e 7 continuam valendo.

## Ciclo TDD

1. **Red:** escrever `tests/test_frete_tdd_regiao.py` **antes** do código. O `pytest` falha com
   `TypeError: calcular_frete() takes 1 positional argument but 2 were given`.
2. **Green:** implementação mínima em `src/frete.py` até todos os testes passarem.
3. **Refactor:** limpar o código (constantes com nome, um bloco por tipo de região)
   mantendo todos os testes verdes.

## Entregáveis

1. `tests/test_frete_tdd_regiao.py` — testes da REQ-05 (criados **antes** do código).
2. `src/frete.py` — implementação da REQ-05.

## Critérios de aceite

- [x] Testes falham antes da implementação (Red).
- [x] `pytest` passa 100% após a implementação (Green), incluindo os testes antigos.
- [x] Fronteiras testadas: R$ 300,00 (ainda paga) e R$ 300,01 (grátis).
- [x] O código referencia a cláusula REQ-05 (rastreabilidade).
