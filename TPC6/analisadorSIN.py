from analisadorLEX import lexer

proxSimb = ("Erro", "",0,0)

def parserError(s):
    print(f'Erro de sintaxe: {s}')

def tokens(simbolo):
    global proxSimb
    if proxSimb is not None and proxSimb.type == simbolo:
        proxSimb = lexer.token()
    else:
        parserError(f'Esperado {simbolo}, encontrado {proxSimb.type}')

def expressao():
    global proxSimb
    if proxSimb.type == "VARIAVEL":
        tokens("VARIAVEL")
        operacao()
        print("Expressão: VARIAVEL")
    elif proxSimb.type == "NUMERO":
        tokens("NUMERO")
        operacao()
        print("Expressão: NUMERO")
    elif proxSimb.type == "PA":
        tokens("PA")
        expressao()
        tokens("PF")
        operacao()
        print("Expressão: PA e PF")
    else:
        parserError(f'Esperado VARIAVEL, encontrado {proxSimb.type}')

def operacao():
    if proxSimb is not None:
        if proxSimb.type == "SOMA":
            tokens("SOMA")
            expressao()
            print("Operação: SOMA")
        elif proxSimb.type == "SUBTRACAO":
            tokens("SUBTRACAO")
            expressao()
            print("Operação: SUBTRACAO")
        elif proxSimb.type == "MULTIPLICACAO":
            tokens("MULTIPLICACAO")
            expressao()
            print("Operação: MULTIPLICACAO")
        elif proxSimb.type == "DIVISAO":
            tokens("DIVISAO")
            expressao()
            print("Operação: DIVISAO")
        elif proxSimb.type == "PF" or proxSimb.type == "eof":
            print("Operação: PF ou EOF")
        else:
            parserError(f'Esperado SOMA, SUBTRACAO, MULTIPLICACAO, DIVISAO ou IGUAL, encontrado {proxSimb.type}')

def atribuicao():
    global proxSimb
    if proxSimb.type == "INPUT":
        tokens("INPUT")
        tokens("VARIAVEL")
        print("Atribuição: '?' VARIAVEL")
    elif proxSimb.type == "VARIAVEL":
        tokens("VARIAVEL")
        tokens("IGUAL")
        expressao()
        print("Atribuição: VARIAVEL '=' expressão")
    elif proxSimb.type == "PRINT":
        tokens("PRINT")
        expressao()
        print("Atribuição: '!' expressão")
    else:
        parserError(f'Esperado INPUT, VARIAVEL ou PRINT, encontrado {proxSimb.type}')

def programa(data):
    global proxSimb
    lexer.input(data)
    proxSimb = lexer.token()
    atribuicao()
    print('Análise sintática concluída')

programa('''
c = a * b / ( a / b )
''')
    