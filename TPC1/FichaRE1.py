import re

line1 = "hello world"
line2 = "goodbye world"
line3 = "hi, hello there"

# o match só procura no inicio da string
# se utilizasse a função search, iria encontrar a palavra hello na linha 3
'''
if re.match(r'hello', line1):
    print("line1: match")
else: 
    print("line1: no match")

if re.match(r'hello', line2):
    print("line2: match")
else:
    print("line2: no match")

if re.match(r'hello', line3):
    print("line3: match")
else:
    print("line3: no match")
'''

line4 = "Hello there! Uh, hi, hello, it's me... Heyyyy, hello? HELLO!"
# print(re.findall(r'hello', line4, re.I)) # re.I é o ignore case
# ou
# print(re.findall(r'(?i:hello)', line4, re.I))

# pesquisar todas as ocorrências de 'hello' dentro da linha, substituindo por '*YEP*'
# print(re.sub(r'hello', r'*YEP*', line4, flags=re.I))

line5 = "bananas, laranjas, maçãs, peras, uvas, melancias, melões, abacaxis e frutos secos etc"
# print(re.split(r',' , line5))
# \s é um espaço em branco 
# * é zero ou mais ocorrências
# print(re.split(r',\s* | e', line5)) 

def palavra_magica (frase):
    return bool(re.search(r'por favor[.!?]$', frase, re.I))

# print(palavra_magica("Posso ir à asa de banho, por favor?"))
# print(palavra_magica("Preciso de um favor."))

# \b é um word boundary
def narcissismo(linha):
    n_eu = len(re.findall(r'\beu\b', linha, flags=re.I))
    # \w+ é uma palavra com um ou mais caracteres
    # se utilizasse um * em vez de um +, iria contar os espaços
    n_pal = len(re.findall(r'\b\w+\b', linha, flags=re.I))
    return  (f' Número de palavras: {n_pal} \n Número de ocorrências da palavra "eu": {n_eu}')

# print(narcissismo("Eu não sei se eu quero continaur a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou")) # 4

def troca_de_curso (linha, novo_curso):
    return re.sub(r'\bLEI\b', novo_curso, linha, flags=re.I)

# print(troca_de_curso("LEI é o melhor curso! Adoro LEI! Porém o curso de LEI é muito difícil", "Engenharia Informática")) # O curso de Engenharia Informática é muito difícil

# \d é um dígito
def soma_string(linha):
    return sum([int(x) for x in re.findall(r'-?\d+', linha)])

print(soma_string("4, -6,2,3,8,-3,0,2,-5,1")) # 6


