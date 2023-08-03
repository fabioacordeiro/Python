'''NAO ESTÁ FUNCIONANDO, VOU VOLTAR NELE MAIS PRA FRENTE
'''
'''
Vou utilizar o conhecimento aprendido em um outro curso
para criar tentar criar um arquivo PDF com o Python'''
# pip install reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

Desc = input('Descreva o orçamento: ')
TT_Horas = int(input('Quantidade de horas estimadas para realizar o trabalho:'))
Valor_hora = int(input('Qual o valor da hora ? :'))
Linguagem = input('Qual a linguagem utilizada para fazer o desenvolvimento ? :')
VlrTT = Valor_hora*TT_Horas
# O arquivo pdf só aceita variáveil string
VlrTexto = str(VlrTT)
TT_Horas_Texto = str(TT_Horas)
Valor_hora_texto = str(Valor_hora)
#Criando o arquivo PDF
''' cria um novo arquivo PDF
pdfFileObj = open('template.pdf', 'wb')'''
pdf = canvas.Canvas('Orçamento.pdf')
#pdf = open('Orçamento.pdf', 'wb')
pdf.save()
pdf.add_page()
pdf.set_font('Arial')
pdf.set_font_size('12')
# Incluindo um template no pdf para ficar mais bonito (O arquivo deve estar na mesma pasta do script)
pdf.image('template.png', x=0, y=0)
pdf.drawString(115, 145, Desc)
pdf.drawString(115, 160, VlrTexto )
pdf.drawString(115, 175, TT_Horas_Texto)
pdf.drawString(115, 195, Valor_hora_texto)
#
pdf.output('Orçamento.pdf')
print('Orçamento gerado com sucesso')



