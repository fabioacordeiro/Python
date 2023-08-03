def leiaDin(txt):
    while True:
        contn = contl = 0
        # contn = contador de numeros , contl = contador de letras
        n = str(input('Digite o preço: \33[32mR$').replace(',', '.')).lower()
        # o replace aceita a virgula ou ponto, o lower passará qualquer possivel letra no texto para minúsculo
        for c in range(0, 10):

            if n.islower():
                # caso foi digitado alguma letra, o lower detectara e somara 1 ao contador validando um erro.
                contl += 1
            if f'{c}' in n:
                # o contador vai de 0 a 9, esse if detecta se c está em n ou seja se do número 0 ao 9 estiver ele detectara e somara ao contador de números.
                contn += 1
        if contn > 0 and contl == 0 and n.count('.') == 1:
            # caso o contador de números seja maior que 0, ou seja há números digitados, e o contador de letras for igual a 0, ou seja com números e sem letras, ele retornara o valor float pois não houve erro.
            return float(n)
        elif contn > 0 and contl == 0 and n.count('.') == 0:
            # caso haja números "contn > 0" e não há letras  ele retornara o valor float pois não houve nenhum erro.
            return float(n)
        elif contl > 0 or n.strip() == '' or n.count('.') > 1:
            # caso o número de letras seja maior que 0, ou seja há letras digitadas, ou caso stripado for igual a vazio, ou o contador de pontos "." que definem o valor decimal seja maior que 1 ou seja se uma pessoa digita o número assim: 5.4.2.3 ele detectara e validara um erro, os counts em cada linha são para verificar se há somente um "." na sua digitação se houver só um: 5.4 ele validará certo se houver mais de um: 5.4.6 ele validará errado.
            print(f'\33[31mERRO! "{n.strip()}" não é um número válido.\33[34m')

