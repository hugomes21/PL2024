from datetime import date
import ply.lex as lex
import re

# Lista de tokens
tokens = (
    'INPUT',
    'VARIAVEL',
    'NUMERO',
    'PRINT',
    'SOMA',
    'SUBTRACAO',
    'MULTIPLICACAO',
    'DIVISAO',
    'IGUAL',
    'PA',
    'PF',
)

# Regras de expressão regular para cada token
t_INPUT = r'\?'         # ? = input
t_VARIAVEL = r'\w+'     # \w+ = qualquer caractere alfanumérico
t_NUMERO = r'\d+'       # \d+ = qualquer dígito
t_PRINT = r'\!'         # ! = print
t_SOMA = r'\+'          # + = soma
t_SUBTRACAO = r'\-'     # - = subtração
t_MULTIPLICACAO = r'\*' # * = multiplicação
t_DIVISAO = r'\/'       # / = divisão
t_IGUAL = r'\='         # = = igual
t_PA = r'\('            # ( = parêntese aberto
t_PF = r'\)'            # ) = parêntese fechado
t_ignore = ' \t\n'        # Caracteres a serem ignorados

# Regra de tratamento de erro
def t_error(t):
    print(f'Caractere ilegal: {t.value[0]}')
    t.lexer.skip(1)

# fim do arquivo
def t_eof(t):
    r'$'
    t.value = None


# Construção do lexer
lexer = lex.lex()

data = '''
? a
b = a * 2 / (27 - 3)
! a + b
c = a * b / ( a / b )
'''

lexer.input(data)
