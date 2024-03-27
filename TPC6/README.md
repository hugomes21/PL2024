# Título
TPC6 - Analisador sintático

# Autor
**Nome:** Hugo Ricardo Macedo Gomes

**ID:** a96842

# Explicação
Construir uma gramática independente de contexto LL(1) para interpretar comandos de uma linguagem de programação simples.

## Comandos como o seguinte:
- ? a
- b = a * 2 / (27 - 3)
- ! a + b
- c = a * b / ( a / b )

## Gramática Independente de Contexto LL(1)
**Terminais:**
- Números: num
- Variáveis: var
- Operadores Aritméticos: + | - | * | /
- Parênteses: ( | )
- Igualdade: =
- Leitura: ?
- Impressão: !

# Funcionamento
Para a resolucao deste TPC, num script em python, criei um analisador léxico e noutro script criei um analisador sintático. 


