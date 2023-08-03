# Faça um programa que leia o sexo de uma pessoa, mas só aceite M ou F
Sexo = str(input('Digite o seu sexo [M/F]:')).strip().upper()[0]#O Strip retira espaços, o Upper coloca maiuscula e [0] pega a primeira letra
while Sexo not in 'MmfF':#Qualquer uma das letras digitadas 'MmfF' ele valida
        Sexo = str(input('Digite o seu sexo [M/F]:')).strip().upper()[0]#O Strip retira espaços, o Upper coloca maiuscula e [0] pega a primeira letra
        if Sexo == 'M':
            print ('Sexo M registrado com sucesso')
        if Sexo == 'F':
            print('Sexo F registrado com sucesso')
print('FIM')