from EX115.Lib.Interface import *
from EX115.Lib.Arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if ArquivoExiste(arq):
    print('Arquivo encontrado com sucesso !!!')
else:
    print('Arquivo não encontrado !!!')
    CriarArquivo(arq)



while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção 1 = Ver pessoas Cadastradas
        LerArquivo(arq)
    elif resposta == 2:
        # Opção 2 = Cadastrar nova Pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Digite um nome:'))
        idade = leiaint('Digite a idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção 3 = Sair do sistema
        cabecalho('Saindo do sistema ... Até logo.')
        break
    else:
        cabecalho('\033[4;30;41mDigite uma opção válida !!!\033[m')
    sleep(0.5)



