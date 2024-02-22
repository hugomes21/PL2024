# Título 
TPC1 - Leitura de um ficheiro csv e resolução de querys

# Autor
**Nome:** Hugo Ricardo Macedo Gomes

**ID:** a96842

# Explicação
Não usufruir do uso de expressões regulares e funções pré-definidas da biblioteca csv, irei apresentar a minha resolução de como fiz a leitura do ficheiro csv e resolução das querys exigidas do TPC1.

## Função parser_csv(filename)
Esta função lê um arquivo CSV linha por linha, divide cada linha em campos usando a função *split()* e retorna uma lista de listas, onde cada lista interna representa uma linha do arquivo CSV.

## Função modadlidades(data)
Esta função recebe os dados do CSV como entrada e retorna uma lista de modalidades (presumivelmente algum tipo de esporte ou evento) ordenada alfabeticamente. A modalidade é extraída da nona coluna (índice 8) de cada linha.

## Função aptos_inaptos(data)
Esta função distribui os atletas por faixa etária. Cada faixa etária é representada por um intervalo de 5 anos (por exemplo, 0-14, 15-19, etc.). A idade do atleta é extraída da sexta coluna (índice 5) de cada linha. A função retorna um dicionário onde as chaves são as faixas etárias e os valores são o número de atletas nessa faixa etária.

## Função main()
Esta é a função principal que é executada quando o scrpit é iniciado. Ela chama as funções acima e imprime os resultados.