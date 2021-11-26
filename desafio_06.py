#Author: Vesley Cesar da Silva
#Data: 24/11/2021
# 06 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

print('=== PROGRAMA EXECUTADO ===')
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print('O dobro do número {} é: {}'.format(numero, dobro))
print('O triplo do número {} é: {}'.format(numero, triplo))
print('A raiz quadrada do número {} é: {:.1f}'.format(numero, raiz))


print('==========================================================')
print('Outra lógica de resolver o mesmo problema')

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print(' O dobro de: {} vale: {} \n O triplo de: {} vale: {} \n A raiz quadrada do número: {} vale: {:.1f}'.format(n, d, n, t, n, r))

print('==========================================================')
print('Outra lógica de resolver o mesmo problema')

x = int(input('Digite um número: '))
print(' O dobro de: {} vale: {} \n O triplo de: {} vale: {} \n A raiz quadrada do número: {} vale: {:.1f}'.format(x, (x*2), x, (x*3), x, pow(x, 1/2)))


