# Relatório de Auditoria — Exercício 2 (Drift e Revisão Multidimensional)

> **Objetivo:** atuar como *Human-in-the-Loop*, comparando o código gerado pela IA
> com a spec EARS (`specs/checkout_frete.md`) e rejeitando tudo que não tem amparo nela.

## 1. O teste de injeção ambígua

Prompt enviado ao agente (de propósito vago, sem cláusula EARS):

> "Implemente a funcionalidade de aplicação de cupom de desconto 'DESCONTO10' para a classe de frete."

Resultado: a IA gerou a função `aplicar_cupom` no commit `e05e11d`
(`experimento(ex2): ...`), adicionando cupons extras, `print` com CPF, um loop
desnecessário e gravação em arquivo — nada disso existe na spec.

**Lição importante:** a suíte de testes continuou **100% verde** com o drift.
Testes só verificam o que foi especificado; não detectam código *a mais*.
Por isso a revisão humana com a matriz abaixo é obrigatória.

## 2. Matriz de Rastreabilidade

Definições:
- **Drift (desvio):** código diverge da spec ou omite cláusula obrigatória.
- **Sobre-implementação:** funcionalidade adicionada "por conta própria" pela IA, sem cláusula EARS.

### 2.1 Antes da correção (commit `e05e11d`)

| Cláusula EARS | Status | Teste Coberto | Arquivo:Linha |
|---|---|---|---|
| REQ-01 (Padrão) | Sim | `test_frete.py:9`, `test_frete.py:15`, `test_frete.py:21` | `frete.py:6`, `frete.py:18`, `frete.py:24` |
| REQ-02 (Grátis) | Sim | `test_frete.py:27`, `test_frete.py:33`, `test_frete.py:39` | `frete.py:8`, `frete.py:14` |
| CUPOM (Sem Spec) | **DRIFT DETECTADO** | Nenhum | `frete.py:30-41` |

### 2.2 Ação de correção mandatória

Prompt ao agente: *"Remova todo o código de cupom sem especificação, restaurando o
alinhamento 100% com a spec."* — `src/frete.py` voltou às 24 linhas da versão Green.

### 2.3 Depois da correção (estado atual)

| Cláusula EARS | Status | Teste Coberto | Arquivo:Linha |
|---|---|---|---|
| REQ-01 (Padrão) | Sim | `test_frete.py:9`, `test_frete.py:15`, `test_frete.py:21` | `frete.py:6`, `frete.py:18`, `frete.py:24` |
| REQ-02 (Grátis) | Sim | `test_frete.py:27`, `test_frete.py:33`, `test_frete.py:39` | `frete.py:8`, `frete.py:14` |
| CUPOM (Sem Spec) | Removido — sem drift | — | — |

> Os números de linha valem para o commit desta auditoria. No Exercício 3 o limite
> da REQ-02 mudou para R$ 250,00 (mesmas linhas) e ganhou o teste de regressão
> `test_frete.py:45` (R$ 200,00 agora paga frete).

## 3. Passe de Revisão Multidimensional

| Dimensão | Pergunta | Versão com drift (`e05e11d`) | Versão corrigida |
|---|---|---|---|
| **Arquitetura** | Respeita o `constitution.md` ou importou lib desnecessária? | ❌ `import json` no meio do arquivo só para persistência não pedida; função sem `REQ-xx` (viola itens 3 e 4 da constituição). | ✅ Sem imports; só biblioteca padrão; toda função cita `REQ-xx`. |
| **Performance** | Existem loops desnecessários no cálculo? | ❌ `for codigo in CUPONS` percorre o dicionário inteiro; bastava `CUPONS.get(cupom)` (O(1)). | ✅ Cálculo O(1): um `if` e uma soma. |
| **Segurança** | Há print de dados sensíveis ou falta de validação? | ❌ `print` com CPF; CPF gravado em texto puro em `cupons_usados.json`; cupom inválido ignorado em silêncio. | ✅ Nenhum print, nenhum dado pessoal, nenhuma escrita em disco. ⚠️ Subtotal negativo/zero não é validado — **não** corrigido aqui porque não há cláusula na spec; a correção certa é o PO criar uma nova cláusula (ex.: `REQ-03 IF subtotal <= 0 THEN THE SYSTEM SHALL rejeitar...`) antes de mexer no código. |
| **Observabilidade** | O código é legível e depurável? | ❌ `print` solto sem padrão (não é log), efeito colateral escondido em arquivo. | ✅ Funções puras, constantes nomeadas, comentários ligando cada linha à spec. |

## 4. Veredito

✅ Código aprovado: 100% alinhado à spec, sem drift e sem sobre-implementação.
