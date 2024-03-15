import json
import re
import time
import math

# load stock from file
def load_stock():
    with open("stock.json", "r") as file:
        # load the stock from the file
        stock = json.load(file)
    return stock['stock']

def load_money():
    with open("stock.json", "r") as file:
        # load the stock from the file
        money = json.load(file)
    return money['saldo']

# save stock to file and decrement the quantity of the chosen product by 1
def save_stock(stock, choice):
    # Load the existing data
    with open("stock.json", "r") as file:
        data = json.load(file)

    # Update the stock
    for item in stock:
        if item['cod'] == choice:
            item['quant'] -= 1
            break

    # Save the updated data
    data['stock'] = stock
    with open("stock.json", "w") as file:
        json.dump(data, file)

def save_money(saldo_moedas, moeda):
    # Load the existing data
    with open("stock.json", "r") as file:
        data = json.load(file)

    # Update the money
    for item in saldo_moedas:
        if item['moeda'] == moeda:
            item['quant'] -= 1

    # Save the updated data
    data['saldo'] = saldo_moedas
    with open("stock.json", "w") as file:
        json.dump(data, file)

# print products available
def print_menu(stock):
    print("Produtos disponíveis:")
    for item in stock:
        print(f"{item['cod']}: {item['nome']} -- {item['preco']}€")

# function that converts the money to euros
def convert_to_euros(s):
    if s:
        match = re.match(r"(\d+)([ec])$", s)
        if match:
            quantidade, moeda = match.groups()
            quantidade = float(quantidade)
            if moeda == 'e':
                return quantidade
            elif moeda == 'c':
                return quantidade / 100
    return 0

# function that calculates the change
def calculate_change(saldo, preco):
    saldo_moedas = load_money()
    troco = saldo - preco
    moedas = sorted(saldo_moedas, key=lambda m: convert_to_euros(m.get('moeda', '0')), reverse=True)
    troco_moedas = {}

    for moeda in moedas:
        valor_moeda = convert_to_euros(moeda.get('moeda', '0'))
        while troco >= valor_moeda and moeda.get('quant', 0) > 0:
            troco = round(troco - valor_moeda, 2)  # round to avoid floating point precision issues
            save_money(saldo_moedas, moeda.get('moeda'))
            if moeda.get('moeda') in troco_moedas:
                troco_moedas[moeda.get('moeda')] += 1
            else:
                troco_moedas[moeda.get('moeda')] = 1

            # If we have already given enough of this coin, move on to the next one
            if troco < valor_moeda:
                break

    # Format the change as a string
    troco_str = []
    for moeda, qtd in troco_moedas.items():
        if moeda is None:
            print("Erro: moeda é None")
        elif not isinstance(qtd, (int, float)):
            print(f"Erro: quantidade não é um número, é {type(qtd)}")
        else:
            troco_str.append(f"{qtd}x {str(moeda)}")

    troco_str = ', '.join(troco_str)
    return troco_str

# algorithm to insert money and give change
def insert_money(chosen_product):
    saldo = 0.0
    print("Insira o dinheiro:")

    while saldo < chosen_product['preco']:
        valor = input()
        valor_convertido = convert_to_euros(valor)
        if valor_convertido == 0:
            print("Valor inválido. Por favor insira um valor válido.")
            continue
        saldo += valor_convertido
    
    print(f"Saldo: {saldo:.2f}€")
    # give change
    troco = calculate_change(saldo, chosen_product['preco'])
    print(f"Troco: {troco}")

    print("-----------------------------------------------------")
    # wait 5 seconds
    time.sleep(5)

# administrator mode which allows to add stock and change prices
def administrator_mode():
    with open("stock.json", "r") as file:
        data = json.load(file)

    stock = data['stock']
    print("Modo administrador")
    print("1 - Adicionar stock")
    print("2 - Alterar preço")
    print("3 - Alterar nome")
    choice = input("Escolha uma opção: ")
    if choice == "1":
        print("Adicionar stock")
        cod = input("Código do produto: ")
        quant = int(input("Quantidade a adicionar: "))
        for item in stock:
            if item['cod'] == cod:
                item['quant'] += quant
                break
    elif choice == "2":
        print("Alterar preço")
        cod = input("Código do produto: ")
        preco = float(input("Novo preço: "))
        for item in stock:
            if item['cod'] == cod:
                item['preco'] = preco
                break
    elif choice == "3":
        print("Alterar nome")
        cod = input("Código do produto: ")
        nome = input("Novo nome: ")
        for item in stock:
            if item['cod'] == cod:
                item['nome'] = nome
                break
    else:
        print("Opção inválida")
        administrator_mode()

    data['stock'] = stock
    with open("stock.json", "w") as file:
        # save the stock to the file
        json.dump(data, file)

def main():
    stock = load_stock()
    while True:
        print_menu(stock)

        choice = input("Escolha um produto: ")
        if choice == "7276":
            administrator_mode()
            stock = load_stock()
            continue

        chosen_product = None
        for item in stock:
            if item['cod'] == choice:
                chosen_product = item
                break

        if chosen_product is None or chosen_product['quant'] == 0:
            print("Produto não disponível")
            time.sleep(2)
            continue

        print(f"Produto escolhido: {chosen_product['cod']}")
        print(f"Preço: {chosen_product['preco']}")

        insert_money(chosen_product)

        save_stock(stock, chosen_product['cod'])

if __name__ == "__main__":
    main()