# Constituição do Projeto

> **O que é este arquivo?** É a "lei maior" do projeto: princípios invioláveis que
> qualquer pessoa ou agente de IA (ex.: Google Antigravity via MCP) deve respeitar
> antes de gerar ou alterar código. Em SDD (Spec-Driven Development), a constituição
> fica acima das specs: uma spec nunca pode contrariar a constituição.

1. Use Python 3.11+ e pytest para todos os testes.
2. Mantenha o código simples e sem dependências externas desnecessárias
   (a única dependência permitida é o `pytest`, usado só para testar).
3. Toda função de produção deve referenciar, em comentário, a cláusula EARS
   (`REQ-xx`) da spec que a justifica (rastreabilidade).
4. Nenhum código pode existir sem uma cláusula correspondente em `specs/`
   (proibida a sobre-implementação).
5. Toda mudança de regra de negócio começa na spec (`specs/`), e spec, testes e
   código devem mudar no **mesmo commit/PR**.
6. Siga o ciclo TDD: primeiro o teste falha (Red), depois a implementação mínima
   faz o teste passar (Green).
