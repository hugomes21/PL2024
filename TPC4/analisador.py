import sys
import ply.lex as lex

# Lista de nomes de tokens reconhecidos pelo analisador léxico
tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'SYMBOL',
    'PARAMETER',
    'VALUE',
    'COMMA',
)

# Tratar do token SELECT
def t_SELECT(lexToken):
    # Definir a expressão regular para o token SELECT
    r'(?i)select'
    return lexToken

# Tratar do token FROM
def t_FROM(lexToken):
    # Definir a expressão regular para o token FROM
    r'(?i)from'
    return lexToken

# Tratar do token WHERE
def t_WHERE(lexToken):
    # Definir a expressão regular para o token WHERE
    r'(?i)where'
    return lexToken

# Tratar do token SYMBOL
def t_SYMBOL(lexToken):
    # Definir a expressão regular para o token RULE
    r'(<=)|(>=)|(==)|(!=)|(<)|(>)|(=)'
    return lexToken

# Tratar do token PARAMETER
def t_PARAMETER(lexToken):
    # Definir a expressão regular para o token PARAMETER
    r'[a-zA-Z_][a-zA-Z_]*'
    return lexToken

# Tratar do token VALUE
def t_VALUE(lexToken):
    # Definir a expressão regular para o token VALUE
    r'\d+'
    return lexToken

# Tratar do token RULE
def t_COMMA(lexToken):
    # Definir a expressão regular para o token COMMA
    r','
    return lexToken

# Tratar de erros
def t_error(lexToken):
    # Imprimir mensagem de erro
    print("Illegal character '%s'" % lexToken.value[0])
    # Ignorar o caracter
    lexToken.lexer.skip(1)

# Tratar de uma nova linha
def t_newline(lexToken):
    # Definir a expressão regular para o token NEWLINE
    r'\n+'
    # Incrementar o número de linhas
    lexToken.lexer.lineno += len(lexToken.value)


# Ignorar espaços e tabs
t_ignore = ' \t'

# Criar uma main que faça o teste do analisador léxico através do terminal
if __name__ == "__main__":
    # Criar um analisador léxico
    lexer = lex.lex()
    
    # Ler a string de input
    for linha in sys.stdin:
        # Passar a string de input para o analisador léxico
        lexer.input(linha)
        # Imprimir os tokens reconhecidos
        for token in lexer:
            print(token)