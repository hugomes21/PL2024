''' Tpc PL ————————— // —————-
Tenho um csv
Nao usar expressões regulares (?)
Proibido usar o modulo csv
Ler linha a linha e “partir” nos campos correspondentes (usar a funcao split)
lista de modalidades ordenada alfabeticamente
Percentagem de atletas aptos e inaptos
Distribuição de atletas por escalão etario(…, [30-34], [35-39], [40-44], …)
'''

def parser_csv(filename):
    with open(filename + '.csv', 'r') as file:
        data = file.readlines()
        data = [line.strip().split(',') for line in data]
    return data

 # lista ordenada alfabeticamente das modalidades desportivas
def modalidades(data):
    modalidades = []
    for line in data:
        modalidades.append(line[8])
    return sorted(set(modalidades), key=str.lower)

# percentagem de atletas aptos e inaptos
def aptos_inaptos(data):
    aptos = 0
    inaptos = 0
    for line in data:
        if line[12] == 'true':
            aptos += 1
        else:
            inaptos += 1
    return (aptos / (aptos + inaptos)) * 100, (inaptos / (aptos + inaptos)) * 100

# distribuição de atletas por escalão etário (…, [30-34], [35-39], [40-44], …)
def escalao_etario(data):
    escalao = {'[0-14]': 0, '[15-19]': 0, '[20-24]': 0, '[25-29]': 0, '[30-34]': 0, '[35-39]': 0, '[40-44]': 0, '[45-49]': 0, '[50-54]': 0, '[55-59]': 0, '[60-64]': 0, '[65-69]': 0, '[70-74]': 0, '[75-79]': 0, '[80-84]': 0, '[85-89]': 0, '[90-94]': 0, '[95-99]': 0, '[100-104]': 0}
    for line in data[1:]:
        if int(line[5]) <= 14:
            escalao['[0-14]'] += 1
        elif int(line[5]) <= 19:
            escalao['[15-19]'] += 1
        elif int(line[5]) <= 24:
            escalao['[20-24]'] += 1
        elif int(line[5]) <= 29:
            escalao['[25-29]'] += 1
        elif int(line[5]) <= 34:
            escalao['[30-34]'] += 1
        elif int(line[5]) <= 39:
            escalao['[35-39]'] += 1
        elif int(line[5]) <= 44:
            escalao['[40-44]'] += 1
        elif int(line[5]) <= 49:
            escalao['[45-49]'] += 1
        elif int(line[5]) <= 54:
            escalao['[50-54]'] += 1
        elif int(line[5]) <= 59:
            escalao['[55-59]'] += 1
        elif int(line[5]) <= 64:
            escalao['[60-64]'] += 1
        elif int(line[5]) <= 69:
            escalao['[65-69]'] += 1
        elif int(line[5]) <= 74:
            escalao['[70-74]'] += 1
        elif int(line[5]) <= 79:
            escalao['[75-79]'] += 1
        elif int(line[5]) <= 84:
            escalao['[80-84]'] += 1
        elif int(line[5]) <= 89:
            escalao['[85-89]'] += 1
        elif int(line[5]) <= 94:
            escalao['[90-94]'] += 1
        elif int(line[5]) <= 99:
            escalao['[95-99]'] += 1
        else:
            escalao['[100-104]'] += 1
    return escalao

def main():
    data = parser_csv('emd')
    print('Lista ordenada alfabeticamente das modalidades desportivas: ')
    print(modalidades(data))
    print('-----------------------------------')
    print('Percentagem de atletas aptos e inaptos: ')
    print(aptos_inaptos(data))
    print('-----------------------------------')
    print('Distribuição de atletas por escalão etário: ')
    print(escalao_etario(data))
    

if __name__ == "__main__":
    main()