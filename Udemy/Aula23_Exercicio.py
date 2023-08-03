'''
Exercicio
veículo em movimento e radar
'''
porc = 0
velocidade = 120 # Velocidade atual do carro
local_carro = 90 # Localização do veículo na estrada

RADAR_1 = 100 #Velocidade máxima do radar
LOCAL_1 = 100 #Localização do radar na estrada
RADAR_RANGE = 1 #Espaço físico de atuação do radar na estrada

excesso_velocidade = velocidade > RADAR_1
Multar = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
if excesso_velocidade and Multar:
    print('Multar o veículo em excesso de velocidade')
print()
porc = (velocidade / RADAR_1) - 1
print(porc)
if porc >= 1:
    print('Multar veículo e suspensão de CNH, velocidade acima de 100%')
elif porc >= 0.5:
    print('Multar veículo, excesso velocidade entre 50.00 % e 99.99%')
elif porc >= 0.199:
    print('Multar veículo, excesso velocidade entre 20 e 49%')
else:
    print('Veículo em velocidade normal')