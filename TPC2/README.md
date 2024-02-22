# Título
TPC2 - Conversor de Markdown para HTML (básico)

# Autor
**Nome:** Hugo Ricardo Macedo Gomes

**ID:** a96842

# Explicação
Utilizando como recurso a libraria 're' (regex) e através do uso de expressões regulares implemntei um conversor simples de Markdow para HTML, tal como solicitado para este TPC, com capacidade de transformar:

- Cabeçalhos (de vários níveis)
- Excerto de texto em negrito
- Excerto de texto em itálico
- Listas numeradas
- Endereços de Links
- Endereços de Imagens
  
## Função headers(line)
Esta função recebe uma linha de texto e procura por cabeçalhos de Markdown, que são linhas que começam com um a seis caracteres '#'. Se encontrar um cabeçalho, substitui-o pelo elemento HTML correspondente.

## Função bold(line)
Esta função recebe uma linha de texto e procura por texto em negrito de Markdown, que é texto envolto em dois asteriscos. Se encontrar texto em negrito, substitui-o pelo elemento HTML correspondente.

## Função italic(line)
Esta função recebe uma linha de texto e procura por texto em itálico de Markdown, que é texto envolto em um asterisco. Se encontrar texto em itálico, substitui-o pelo elemento HTML correspondente.

## Função ordered_list(line)
Esta função recebe uma linha de texto e procura por itens de lista ordenada de Markdown, que são linhas que começam com um número seguido de um ponto. Se encontrar um item de lista, substitui-o pelo elemento HTML correspondente.

## Função link(line)
Esta função recebe uma linha de texto e procura por links de Markdown, que são texto envolto em colchetes seguido de um URL envolto em parênteses. Se encontrar um link, substitui-o pelo elemento HTML correspondente, com o URL como o atributo href.

## Função image(line)
Esta função recebe uma linha de texto e procura por imagens de Markdown, que são texto envolto em colchetes precedido por um ponto de exclamação e seguido de um URL envolto em parênteses. Se encontrar uma imagem, substitui-a pelo elemento HTML correspondente com o URL como o atributo src e o texto como o atributo alt.

## Função markdown_to_html(markdown)
Esta é a função principal que coordena a conversão de Markdown para HTML. Recebe um texto em Markdown, divide-o em linhas, e para cada linha, aplica as funções de conversão acima na ordem correta. Concatena todas as linhas convertidas em uma única string HTML.

## Função main()
Esta função lê um arquivo de texto em Markdown, converte-o para HTML usando a função markdown_to_html, e escreve o HTML resultante em um novo arquivo. Atualmente, os nomes dos arquivos de entrada e saída são codificados como 'exemplo.md' e 'resultado.html', respectivamente.

