# PyPDF2 para manipular arquivos PDF (PdfWriter)
# PyPDF2 para manipular arquivos PDF (PdfMerger)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path


#@ @ -9, 7 + 9, 7 @ @
pip install pypdf2
PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'


#@ @ -39, 3 + 39, 17 @ @
with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
    writer.add_page(page)
    writer.write(arquivo)  # type: ignore


files = [
    PASTA_NOVA / 'page1.pdf',
    PASTA_NOVA / 'page0.pdf',

]

merger = PdfMerger()
for file in files:
    merger.append(file)  # type: ignore

merger.write(PASTA_NOVA / 'MERGED.pdf')  # type: ignore
merger.close()
