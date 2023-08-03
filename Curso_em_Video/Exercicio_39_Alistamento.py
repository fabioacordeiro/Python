# Faça um programa que leia a data de nascimento informada e informe o ano de alistamento, se é hora de se alistar
# se já passou do prazo, e os tempos faltantes para se alistar e quanto passou do prazo.
# Estou aqui em 11/01/2022 12:35 teste de Covid positivo, e para passar o tempo mergulhado no aprendizado da linguagem sensacional python
# fazendo os cálculos de quando meu filho Lucas Cordeiro da Silva vai se alistar ele nasceu em 2018, amo demais meu garoto
# hoje só uma criança e em 14 anos será um homem, Deus te abençoe meu querido, são os votos do seu pai Fábio Alves Cordeiro
# Conselho, Faça algo de bom e deixe um legado de coisas boas, se possível faça algo que ajude milhares de pessoas;

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento :'))
idade = atual - nasc
print ('Quem nasceu em {} tem {} ano(s), em {}.'.format(nasc, idade,atual))
alistamento = nasc+18
if alistamento > atual:
    falta = alistamento - atual
    print ('Você deve se alistar em {}, falta {} ano(s)'.format(alistamento,falta))
elif alistamento < atual:
     passou = atual - alistamento
     print('Você já passou do prazo em {} anos, deveria ter se alistado em {}'.format(passou,alistamento))
elif alistamento == atual:
    print('Corra você deve se alistar imediatamente em {}'.format(alistamento))
