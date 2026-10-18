# Roteiro de Testes — Módulo de Cálculo de Frete (TASK-01) frete.py

## Introdução

As regras de negócio testadas seguem o documento `specs/checkout_frete.md`:

- **REQ-01:** a taxa de frete padrão é de R$ 15,00.
- **REQ-02:** a partir de um subtotal de R$ 250,00 (inclusive), o frete é gratuito.
- **REQ-03:** ao confirmar o frete, a taxa local vem do serviço externo de logística (`ServicoLogisticaAPI`).
- **REQ-04:** ao confirmar o frete, o cliente recebe exatamente 1 notificação de rastreio com o ID do pedido.
- **REQ-05:** Norte e Nordeste pagam R$ 10,00 a mais, exceto com subtotal superior a R$ 300,00 (frete grátis).

## Testes Unitários

Os testes unitários verificam a função `calcular_frete` de forma isolada, sem nenhuma dependência de outras funções. O foco está nos valores de fronteira da REQ-02, já que é ali que o comportamento da função muda.

## Testes de Integração

Os testes de integração verificam se a função `calcular_total` e a função `calcular_frete` funcionam corretamente quando conectadas, sem o uso de mock. Isso garante que o total do pedido é calculado corretamente somando o subtotal à taxa de frete real, calculada pela própria função `calcular_frete`.

## Testes Funcionais

Os testes funcionais avaliam o comportamento do sistema do ponto de vista do usuário, sem se preocupar com os detalhes internos da implementação. O foco está no resultado final que o usuário percebe ao finalizar uma compra.

## Testes Unitários com padrão AAA (Lab 8, Ex. 7.1)

Arquivo `test_frete_unitario_aaa.py`. Cada teste é dividido em três fases: *Arrange* (prepara o subtotal e o frete esperado), *Act* (chama `calcular_frete` uma única vez) e *Assert* (compara o resultado). Os valores testados são R$ 100,00, R$ 249,99, R$ 250,00 e R$ 250,01.

## Testes com Test Doubles (Lab 8, Ex. 7.2)

A função `confirmar_frete` depende de dois serviços externos que não podem ser chamados de verdade nos testes. Eles são substituídos por *Test Doubles*:

- **Dummy:** o parâmetro `usuario` recebe um objeto qualquer (`object()`), porque a lógica não usa.
- **Stub:** o `ServicoLogisticaAPI` devolve uma taxa fixa programada (`return_value`), sem rede.
- **Mock:** o `ServicoNotificacao` é conferido depois da execução (`assert_called_once_with`).
- **Spy:** `patch(..., wraps=...)` deixa o `calcular_frete` real rodar e registra a chamada.

O entregável é `test_frete_unitário_com_doubles.py`; os arquivos `test_frete_doubles_dummy.py`, `test_frete_doubles_stub.py` e `test_frete_doubles_mock.py` mostram cada papel separado, para estudo.

## TDD da regra regional (Lab 8, Ex. 7.4)

O arquivo `test_frete_tdd_regiao.py` foi escrito antes do código (Red: `TypeError`, porque `calcular_frete` ainda não aceitava a região). Depois veio a implementação mínima (Green) e a limpeza do código (Refactor), sempre com todos os testes verdes. Os testes cobrem as fronteiras R$ 300,00 (ainda paga, pois a regra diz "superior a") e R$ 300,01 (grátis), e garantem que as outras regiões continuam seguindo REQ-01 e REQ-02.

## Considerações Finais

Os testes unitários isolam a lógica de cálculo do frete, garantindo que as regras de negócio (REQ-01 e REQ-02) estão corretamente implementadas nos pontos de fronteira. Os testes de integração confirmam que `calcular_total` e `calcular_frete` interagem corretamente, sem a necessidade de simular (mockar) nenhuma das duas funções. Já os testes funcionais validam a experiência do usuário final, garantindo que o valor exibido no checkout está de acordo com o esperado em diferentes cenários de compra. Por fim, os Test Doubles permitem testar a confirmação do frete sem depender de serviços externos, e o TDD garantiu que a regra regional (REQ-05) nasceu já coberta por testes.
