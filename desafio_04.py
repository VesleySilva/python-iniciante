#Author: Vesley Cesar da Silva
#Data: 23/11/2021
# 04 - Faça um programa que leia algo pelo o teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele


n1 = input('Digite algo: ')
print('O seu tipo primitivo é: ', type(n1))
print('Ele é do tipo Alfanumérico: ', n1.isalnum())
print('Ele é caracter: ', n1.isalpha())
print('Ele é do tipo Numérico: ', n1.isnumeric())
print('Ele é está em caixa alta: ', n1.isupper())
print('Ele está em caixa baixa: ', n1.islower())
