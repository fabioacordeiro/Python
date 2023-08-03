# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4
import re

import requests
from bs4 import BeautifulSoup

# url = 'http://127.0.0.1:3333/'
# Vamos fazer uma raspagem de dados na própria biblioteca do BeatifulSoup
url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')
soup = parsed_html
print(f'{"soup.title":.^70}')
if parsed_html.title is not None:
    print(parsed_html.title.text)
print(70*'-')
print(f'{"soup.title.parent.name":.^70}')
if soup.title.parent.name is not None:
    print(soup.title.parent.name)
print(70*'-')
print(f'{"soup.p":.^70}')
if soup.p is not None:
    print(soup.p)
print(70*'-')

print(f'{"soup.a":.^70}')
print(soup.a)
print(f'{"soup.find_all(a)":.^70}')
print(soup.find_all('a'))
print(70*'-')
print(f'{"for link in soup.find_all(a):":.^70}')
print(f'{"print(link.get(href)":.^70}')
for link in soup.find_all('a'):
    print(link.get('href'))

print(f'{"Pegando todo o texto de uma página com o soup.get_text()":.^70}')
print(soup.get_text())

print(f'{"Ver codificação do head para saber a codificação se é utf8 ou não":.^70}')
print(f'{"head tem uma filha, mas possui 2 decendentes":.^70}')
print(soup.head)
print(f'Filha:{len(list(soup.children))}')
print(f'Descendentes:{len(list(soup.descendants))}')

'''
print(f'{"soup.p[class]":.^70}')
if soup.p is not None:
    print(soup.p["reference external"])
print(70*'-')
'''

'''
top_jobs_heading = parsed_html.select('#inicio-rapido')
# print(top_jobs_heading)

if top_jobs_heading is not None:
    article = top_jobs_heading.parent

    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())

'''
# print(parsed_html)
