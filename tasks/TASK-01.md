# TASK-01 — Frete padrão e frete grátis por valor

> **Task atômica:** uma unidade de trabalho pequena o bastante para o agente de IA
> executar de uma vez, sem precisar ver o projeto inteiro.

## Contexto fornecido ao agente (isolamento estrito)

Forneça ao agente **apenas**:
- `constitution.md`
- `specs/checkout_frete.md`
- este arquivo (`tasks/TASK-01.md`)

Nunca envie o projeto inteiro (evita alucinação e sobre-implementação).

## Escopo (tamanho mínimo)

- Cobre **apenas** o cálculo de frete padrão (REQ-01) e o frete grátis por valor (REQ-02).

## Entregáveis

1. `tests/test_frete.py` — suíte pytest para REQ-01 e REQ-02 (criada **antes** do código).
2. `src/frete.py` — implementação mínima que faz os testes passarem.

## Critérios de aceite

- [x] Testes falham antes da implementação (Red).
- [x] `pytest` passa 100% após a implementação (Green).
- [x] O código referencia as cláusulas REQ-01 e REQ-02 (rastreabilidade).

## Prompts usados no Antigravity

1. *Teste:* "Leia TASK-01.md e specs/checkout_frete.md. Crie a suíte pytest em
   tests/test_frete.py para REQ-01 e REQ-02. Não crie o código de implementação ainda."
2. *Implementação:* "Crie src/frete.py com o código ESTRITAMENTE necessário para
   fazer os testes passarem. Proibido código extra."
