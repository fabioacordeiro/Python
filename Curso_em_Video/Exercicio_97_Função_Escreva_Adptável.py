#Faça uma função com o comando escreva adaptável ao tamanho da mensagem que solicitou;

def escreva(msg):
    tam = len(msg)+4
    print('='* tam)
    print(f'{msg:^{tam}}')
    print('=' * tam)

#Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')