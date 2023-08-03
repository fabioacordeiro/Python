'''
vamos aprender sobre set ou conjuntos
'''
# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio
print(s1)
s1 = {'Luiz', 1, 2, 3}  # com dados
print(s1)

print('Vamos retirar os valores duplicados de uma lista')
L1 = [1, 2, 2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6,6,6,6,7,7,7,7,8,8,8,9]
print(f'L1:{L1}')
L2 = [10, 10, 10, 11,11,11,12,13,14,14,14,15,14,12,12,11,10,9,8,7]
print(f'L2:{L2}')
L3 = L1 + L2
s1 = set(L3)
L4 = list(s1)
print(f'L4 unindo L1 e L2 e retirando duplicatas:{L4}')

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard
s2 = set()
print('Adicionando valor com o add')
s2.add('Luiz')#O método add adiciona somente um valor por vez
print(s2)
s2.add(1)
s2.update('Ola Mundo')# Este método inseri um valor por vez
print(f'Adicinando valores com update:{s2}')
s2.update(('Olá Mundo',1,2,3,4,5,'Helloooou'))
print(f'Adicinando valores com update usando 2 parenteses:{s2}')
s2.discard('Helloooou')
s2.discard(' ')
s2.discard('O')
s2.discard('l')
s2.discard('a')
s2.discard('M')
s2.discard('u')
s2.discard('n')
s2.discard('d')
s2.discard('o')

print(f'Deletando os valores com discard():{s2}')
# Operadores úteis:
# união | união (union) - Une
print('Unindo os valores de 2 planos')
s3 = set()
s4 = set()
s5 = set()
s3 = {1,2,3}
print(f's3:{s3}')
s4 = {2,3,4}
print(f's4:{s4}')
s5 = s3 | s4
s5 = s3 & s4 # Ou este comando, é o mesmo do de cima
print(f'Unindo os valores de s3 e s4 em s5:{s5}')
s5 = s3 - s4 #Queremos ver somente os dados que estão disponíveis em s3 e diferentes de s4
print(f'Fazendo a diferença entre planos s3 - s4:{s5}')
s5 = s4 - s3 #Queremos ver somente os dados que estão disponíveis em s4 e diferentes de s3
print(f'Fazendo a diferença entre planos s4 - s3:{s5} estão disponíveis em s4 e diferentes de s3')
s5 = s3 ^ s4 #Queremos ver somente os dados que não estão disponíveis em ambos, neste caso não importa a ordem
print(f'Fazendo a diferença simétrica s3 ^ s4:{s5} não estão disponíveis em ambos a ordem não importa')


# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
