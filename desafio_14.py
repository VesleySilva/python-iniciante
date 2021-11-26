#Author: Vesley Cesar da Silva
#Data: 24/11/2021

# 14 - Faça um algoritmo que o usuário digita a temperatura em graus Celsius e ele converte para Fahrenheit

print('=== PROGRAMA EXECUTADO ===')
celsius = float(input('Digite quantos graus Celsius está fazendo hoje: '))
conv_f = (celsius * (9/5)) + 32
print('{:.2f} °C convertido em Fahrenheit dá °F: {:.2f}'.format(celsius, conv_f))
conv_k = (celsius + 273.15)
print('{:.2f} °C convertido em °K dá: {:.2f}'.format(celsius, conv_k))

print('=' * 58)
print('Resolvendo mesmo problema com uma lógica diferente')
c = float(input('Informe a temperatura em °C: '))
f = ((9 * c)/5) + 32
conv = (celsius + 273.15)
print('A temperatura de {:.2f} °C corresponde a {:.2f} °F !'.format(c, f))
print('A temperatura de {:.2f} °C corresponde a {:.2f} °K !'.format(c, conv))
