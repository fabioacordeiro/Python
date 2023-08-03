Celsius = float(input('Digite a temperatura em graus Celsius :'))
Res = ((9*Celsius)/5)+32
print ('A temperatura {}ºC é {}ºF'.format(Celsius, Res))

Fare = float(input('Digite a temperatura em Fahrenheit para conversão em Celsius :'))
Result = ((Fare-32)/9)*5
print ('A temperatura de {}ºF equivale {:.2f}ºC'.format (Fare,Result))