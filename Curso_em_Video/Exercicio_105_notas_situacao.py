#Faça um programa que tenha a função notas() que pode receber várias notas de alunos e vai retornar um dicionário
#com as seguintes informações:
#Quantidade de notas:
#A maior nota;
#A menor nota;
#A média da turma;
#A situação opcional (sit); Boa (>7), Razoável (7> and > 5) e Ruim(<5)
#Adicione também as docstrings (manual da função);

def notas(*n, sit=False):
        """
        ----> Programa para analisar notas e situação de vários alunos.
        :resp: As notas de 1 ou mais alunos
        :sit: Boa (>7), Razoável (7> and > 5) e Ruim(<5)
        :return: Um dicionário com a maior nota, menor nota, média nota
        """
        notas2 = dict()
        notas2["Total"] = len(n)
        notas2["Maior"] = max(n)
        notas2["Menor"] = min(n)
        notas2["Média"] = sum(n) / len(n)
        if sit == True:
            if notas2["Média"] >= 7:
                notas2["Situação"] = "Boa"
            elif notas2["Média"] <= 5:
                notas2["Situação"] = "Ruim"
            else:
                notas2["Situação"] = "Razoável"
        return notas2


resp = notas(3.2, 3.5, 14.5, 6.5, sit=True)
print(resp)
help(notas)
