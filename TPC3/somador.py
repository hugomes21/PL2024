import re

def somador(file):
    res = 0
    somar = True
    linha = 0

    for line in file:
        linha += 1
        # Encontra todas as sequências de dígitos no texto
        digitos = re.findall(r'\d+|On|Off|=', line, re.IGNORECASE)

        for digito in digitos:
            if digito.isdigit() and somar:
                res += int(digito)
            elif digito.lower() == 'off':
                somar = False
            elif digito.lower() == 'on':
                somar = True
            elif digito.lower() == '=':
                print(f'Resultado da linha {linha}: {res}')
                res = 0
                somar = True

# Exemplo de uso
with open('exemplo.csv', 'r') as file:
    somador(file)
