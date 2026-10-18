# TASK-02 — Confirmação do frete com serviços externos (Lab 8, Ex. 7.2)

> **Task atômica:** uma unidade de trabalho pequena o bastante para o agente de IA
> executar de uma vez, sem precisar ver o projeto inteiro.

## Contexto fornecido ao agente (isolamento estrito)

Forneça ao agente **apenas**:
- `constitution.md`
- `specs/checkout_frete.md`
- este arquivo (`tasks/TASK-02.md`)

## Escopo (tamanho mínimo)

- Cobre **apenas** REQ-03 e REQ-04: a função `confirmar_frete` e as interfaces
  `ServicoLogisticaAPI` e `ServicoNotificacao`.
- A assinatura de `confirmar_frete` recebe `usuario` (sessão do usuário logado), exigido
  pela interface do checkout, mas **não** usado no cálculo. No teste ele é um *Dummy*.
- Os serviços reais não existem no laboratório: seus métodos lançam `NotImplementedError`.
  Se um teste usar o serviço real por engano, ele quebra na hora (garante o isolamento).

## Entregáveis

1. `tests/test_frete_unitário_com_doubles.py` — teste isolado com Dummy, Stub e Mock
   (entregável do Ex. 7.2).
2. `tests/test_frete_doubles_dummy.py`, `tests/test_frete_doubles_stub.py` e
   `tests/test_frete_doubles_mock.py` — um arquivo por papel, para estudo.
3. `src/frete.py` — `confirmar_frete`, `ServicoLogisticaAPI` e `ServicoNotificacao`.

## Critérios de aceite

- [x] Nenhum teste faz chamada de rede real (os serviços são substituídos por Test Doubles).
- [x] O Stub devolve uma taxa fixa programada e o total do pedido usa essa taxa.
- [x] O Mock confirma que `enviar_notificacao_rastreio()` foi chamado exatamente 1 vez,
      com o ID correto do pedido.
- [x] O código referencia as cláusulas REQ-03 e REQ-04 (rastreabilidade).
