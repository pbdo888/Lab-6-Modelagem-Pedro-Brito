# Roteiro de Testes — Módulo de Cálculo de Frete (TASK-01) frete.py

## Introdução

As regras de negócio testadas seguem o documento `specs/checkout_frete.md`:

- **REQ-01:** a taxa de frete padrão é de R$ 15,00.
- **REQ-02:** a partir de um subtotal de R$ 250,00 (inclusive), o frete é gratuito.

## Testes Unitários

Os testes unitários verificam a função `calcular_frete` de forma isolada, sem nenhuma dependência de outras funções. O foco está nos valores de fronteira da REQ-02, já que é ali que o comportamento da função muda.

## Testes de Integração

Os testes de integração verificam se a função `calcular_total` e a função `calcular_frete` funcionam corretamente quando conectadas, sem o uso de mock. Isso garante que o total do pedido é calculado corretamente somando o subtotal à taxa de frete real, calculada pela própria função `calcular_frete`.

## Testes Funcionais

Os testes funcionais avaliam o comportamento do sistema do ponto de vista do usuário, sem se preocupar com os detalhes internos da implementação. O foco está no resultado final que o usuário percebe ao finalizar uma compra.

## Considerações Finais

Os testes unitários isolam a lógica de cálculo do frete, garantindo que as regras de negócio (REQ-01 e REQ-02) estão corretamente implementadas nos pontos de fronteira. Os testes de integração confirmam que `calcular_total` e `calcular_frete` interagem corretamente, sem a necessidade de simular (mockar) nenhuma das duas funções. Já os testes funcionais validam a experiência do usuário final, garantindo que o valor exibido no checkout está de acordo com o esperado em diferentes cenários de compra.
