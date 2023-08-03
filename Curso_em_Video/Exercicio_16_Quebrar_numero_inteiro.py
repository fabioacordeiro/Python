#Programa para quebrar um numero fracionado para inteiro
import math
num = float (input('Digite um número fracionado qualquer :'))
num2 = math.trunc(num)
print ('O numero quem você digitou é {} e o número inteiro é {}'.format (num, num2))