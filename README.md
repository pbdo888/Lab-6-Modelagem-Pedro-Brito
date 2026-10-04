# Lab 6 — Modelagem de Sistemas: SDD, MCP e Revisão Multidimensional

Laboratório prático (Mackenzie) sobre **Spec-Driven Development (SDD)** aplicado a um
cálculo de frete de checkout, com TDD (pytest), auditoria de *drift* e spec viva.

## Estrutura

| Arquivo | Papel |
|---|---|
| `constitution.md` | Princípios invioláveis do projeto (acima das specs). |
| `specs/checkout_frete.md` | Spec em notação EARS — Fonte Única da Verdade (SSOT). |
| `tasks/TASK-01.md` | Task atômica entregue ao agente de IA. |
| `tests/test_frete.py` | Suíte pytest (escrita antes do código). |
| `src/frete.py` | Implementação mínima. |
| `audit_report.md` | Matriz de rastreabilidade + passe multidimensional (Ex. 2). |
| `pytest.ini` | Faz o pytest achar `src/` e `tests/`. |

## Como rodar

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows (no Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt
pytest -v
```

No PyCharm: abra a pasta, selecione o interpretador `.venv` e rode `pytest` no terminal
(ou clique com o botão direito em `tests/` → *Run 'pytest in tests'*).

## Os 3 exercícios no histórico do Git

| Exercício | Commit / Branch | O que mostra |
|---|---|---|
| Setup | `chore: setup SDD ...` | Constituição, spec EARS e TASK-01 antes de qualquer código. |
| 1 — Red | `test(frete): ... (TDD - Red)` | Testes criados; `pytest` falha com `ModuleNotFoundError`. |
| 1 — Green | `feat(frete): implementacao minima ...` | `src/frete.py` mínimo; 6 testes passam. |
| 2 — Drift | `experimento(ex2): ...` | Código de cupom gerado por prompt ambíguo (testes continuam verdes!). |
| 2 — Correção | `fix(frete): remove cupom sem spec ...` | Cupom removido + `audit_report.md`. |
| 3 — Spec viva | branch `feat/frete-gratis-250` (PR) | Spec, testes e código mudam **no mesmo commit** (R$ 200 → R$ 250). |

## Resumo para a prova

- **Requisito zumbi / vibe coding:** pedir código à IA "no feeling", sem spec → código sem garantias.
- **EARS:** sintaxe controlada para requisitos sem ambiguidade.
  - *Ubiquitous:* `THE SYSTEM SHALL ...` (vale sempre) → REQ-01.
  - *Event-driven:* `WHEN <evento>, THE SYSTEM SHALL ...`.
  - *State-driven:* `WHILE <estado>, THE SYSTEM SHALL ...`.
  - *Unwanted behaviour:* `IF <condição>, THEN THE SYSTEM SHALL ...` → REQ-02.
  - *Optional feature:* `WHERE <recurso existe>, THE SYSTEM SHALL ...`.
- **SSOT:** a spec é a única fonte da verdade; se código e spec divergem, o código está errado.
- **Constituição:** regras globais (linguagem, dependências, rastreabilidade) que o agente lê via **MCP**
  (Model Context Protocol = protocolo que dá ao agente acesso ao contexto do projeto).
- **1 task por vez / isolamento:** o agente recebe só constituição + spec + task, nunca o projeto todo.
- **TDD:** Red (teste falha porque o código não existe) → Green (código mínimo passa) → (Refactor).
- **Drift:** código diverge da spec ou omite cláusula. **Sobre-implementação:** IA adiciona coisa sem cláusula.
- **Testes verdes não provam ausência de drift:** eles não enxergam código *a mais* → revisão humana.
- **Human-in-the-Loop:** o aluno é o validador que rejeita código sem amparo na spec.
- **Passe multidimensional:** Arquitetura, Performance, Segurança, Observabilidade.
- **Regra de ouro do SDD:** nunca altere o código primeiro; a mudança começa na spec.
- **Regra inegociável:** spec + testes + código no mesmo commit/PR; PR só com código é rejeitado.
- **Commit padronizado (Conventional Commits):** `tipo(escopo): descrição` — ex.: `feat(frete): ...`.
