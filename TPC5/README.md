# Título
TPC5 - Programa que simule uma máquina de vending

# Autor
**Nome:** Hugo Ricardo Macedo Gomes

**ID:** a96842

# Explicação
*Script* que simule uma máquina de vending. A máquina tem um stock de produtos, uma lista de triplos: nome do produto, quantidade e preço.

É necessário apresentar uma interação com a máquina, assim que esta é ligada, para se poder perceber o tipo de comandos que a máquina aceita.

## Exemplo de um produto
"stock" = [ 
    {"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7}, 
    ... 
]

## Exemplo do saldo da máquina
"saldo": [
    {"moeda": "2e", "quant": 100},
    ...
]

# Funcionamento
O programa é iniciado e mostra, no terminal, todos os produtos, os seus respetivos códigos e preços.

O programa fica à espera que o utilizador escolha um produto e essa escolha só é conseguida através do código do produto desejado. O programa confirma essa escolha e indica o preço, ficando à espera que o utilizador insira o dinheiro. So é possível inserir moedas de 2 e 1 euros, de 50, 20, 10, 5, 2 e 1 cêntimos. O programa espera que o utilizador meta o valor correto e indica o saldo ou, se ultrapassar o valor do produto calcula o troco.

Decidi implementar um modo de administrador que só é acedido com um código especial, neste caso **7276**. Dentro deste modo, posso adicionar stock, alterar o preço e alterar o nome dos produtos!
