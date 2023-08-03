# PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 para manipular arquivos PDF (PdfReader)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2


from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter

PDF_Raiz = Path(__file__).parent
PDF_Original = PDF_Raiz / 'PDF_Original'
PDF_Novo = PDF_Raiz / 'PDF_Novo'
Rel_Bacen = PDF_Original / 'Rel_focus.pdf'
print(PDF_Raiz)
print(PDF_Original)
print(PDF_Novo)
print(Rel_Bacen)

reader = PyPDF2.PdfReader(Rel_Bacen)
print(len(reader))

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]
imagem0 = page0.images[0]

# print(page0.extract_text())
# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)  # type: ignore
