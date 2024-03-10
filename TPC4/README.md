# Título
TPC4 - Analisador Léxico para uma linguagem de query

# Autor
**Nome:** Hugo Ricardo Macedo Gomes

**ID:** a96842

# Explicação
*Script* que implementa um analisador léxico usando a bibliotea Ply que permite definir *tokens* de expressões simples de SQL.

## Tokens Reconhecidos
- SELECT;
- FROM;
- WHERE;
- SYMBOL;
- PARAMETER;
- VALUE;
- COMMA;
  
O *script* ignora espaços em branco, tabs e carateres *newline*.
Caracteres que não estejam definidos são considerados como ilegais.
Por fim, este *script* funciona através de input através do terminal, identifica os *tokens* e imprime-os no terminal conforme o que tiver sido identificado.