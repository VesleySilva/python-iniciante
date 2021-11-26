#Author: Vesley Cesar da Silva
#Data: 24/11/2021
# 13 - Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento

print('=== PROGRAMA EXECUTADO ===')
salario = float(input('Digite o salário do funcionário: '))
sala_con = (salario * 0.15)
sala_fin = (sala_con + salario)
print('O antigo salário do cliente era de: {:.2f} depois do aumento de 15% ele passou a ganhar: {:.2f}'.format(salario, sala_fin))

print('=' * 58)
print('Resolvendo o mesmo problema com uma lógica diferente')
sal = float(input('Qual é o salário do funcionário R$: '))
novo = sal + (sal * 15 / 100)
print('Um funcionário que ganhava R$: {:.2f} depois do aumento de 15 % passou a receber o valor de R$: {:.2f}'.format(sal, novo))
