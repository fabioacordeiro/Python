from EX115.Lib.Interface import *


def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError: #Se o arquivo não for encontrado então gera um erro
        return False
    else:
        return True


def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')#Significa w de Writer e t de Texto e + adicionar caso não exista
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo !!!')
    else:
        print(f'Arquivo {nome} criado com sucesso !!!')


def LerArquivo(nome):
    try:
        a = open(nome, 'rt')#Significa r de Read e t de Texto
    except:
        print('Erro ao ler o arquivo !!!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.upper().split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')#Significa a de Atualizar e t de Texto
    except:
        print('Erro ao ler o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de registrar os dados!!! ')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()



