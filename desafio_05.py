#Author: Vesley Cesar da Silva
#Data: 24/11/2021
# 05 - Faça um programa que insere um número e ele exibe na tela o sucessor e antecessor desse número

print('=== PROGRAMA EXECUTADO ===')
numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1
print('O antecessor do número {} é: {}'.format(numero, antecessor))
print('O sucessor do número {} é: {}'.format(numero, sucessor))


print('==========================================================')
print('Outra lógica de resolver o mesmo problema')

n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando o valor: {}, seu antecessor é: {} e o seu sucessor é: {}'.format(n, a, s))


print('==========================================================')
print('Outra lógica de resolver o mesmo problema')
n = int(input('Digite um número: '))
print('Analisando o valor: {}, seu antecessor é: {} e o seu sucessor é: {}'.format(n, (n-1), (n+1)))
