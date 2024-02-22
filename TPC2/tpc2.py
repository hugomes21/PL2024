import re

# Criar um conversor de Makrdowm para HTML

# função que transforma linhas iniciadas por # em h1, ## em h2, etc
def headers(line):
    return re.sub(r'^(#{1,6})(.*)$', lambda x: f'<h{x.end(1)-x.start(1)}>{x.group(2).strip()}</h{x.end(1)-x.start(1)}>', line)

# função que transforma linhas iniciadas por ** em <b>
def bold(line):
    return re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)

# função que transforma linhas iniciadas * em <i>
def italic(line):
    return re.sub(r'\*(.*?)\*', r'<i>\1</i>', line)

# função que transforma linhas iniciadas por 1., 2., 3., etc em <ol>
def ordered_list(line):
    if re.match(r'\d+\.', line):
        return f'<ol><li>{line[3:]}</li></ol>'
    return line

# função que transforma linhas iniciadas por [texto](endereço URL) em <a> href="endereço URL" texto </a>
def link(line):
    if re.match(r'\[.*\]\(.*\)', line):
        h = line.find('[')
        i = line.find(']')
        j = line.find('(')
        k = line.find(')')
        return f'<a href="{line[j+1:k]}">{line[h+1:i]}</a>'
    return line

# função que transforma linhas iniciadas por ![texto](path para imagem) em <img> src="path para imagem" alt="texto" </img>
def image(line):
    if re.match(r'\!\[.*\]\(.*\)', line):
        h = line.find('[')
        i = line.find(']')
        j = line.find('(')
        k = line.find(')')
        return f'<img src="{line[j+1:k]}" alt="{line[h+1:i]}">'
    return line

# função que transforma o markdown em html
def markdown_to_html(markdown):
    html = ''
    in_ordered_list = False
    for line in markdown.split('\n'):
        if re.match(r'\d+\.', line):
            if not in_ordered_list:
                in_ordered_list = True
                html += '<ol>\n'
            line = '<li>' + line[line.find('.')+2:] + '</li>'
        else:
            if in_ordered_list:
                in_ordered_list = False
                html += '</ol>\n'
            line = headers(line)
            line = bold(line)
            line = italic(line)
            line = link(line)
            line = image(line)
        
        html += line + '\n'
    
    if in_ordered_list:
        html += '</ol>\n'
    
    return html

def main():
    # buscar o arquivo markdown
    with open('exemplo.md', 'r') as file:
        markdown = file.read()
    # converter o markdown para html
    html = markdown_to_html(markdown)
    # salvar o html
    with open('resultado.html', 'w') as file:
        file.write(html)

main()