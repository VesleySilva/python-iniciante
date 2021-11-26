#Author: Vesley Cesar da Silva
#Data: 24/11/2021
# 07 - Desenvolva um programa que lê as duas notas de um aluno e calcule a sua média

print('=== PROGRAMA EXECUTADO ===')
nome = input('Digite o seu nome: ')
nota_p = float(input('Digite a primeira nota: '))
nota_s = float(input('Digite a segunda nota: '))
media = (nota_s + nota_p) / 2
print('A primeira nota foi: {} e a segunda nota foi: {} '.format(nota_p, nota_s))
print('O aluno: {} ficou com a média de: {:.1f}'.format(nome, media))

print('==========================================================')
print('Outra lógica de resolver o mesmo problema')

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1+n2)/2
print('A média entre {} e {} é igual: {}'.format(n1, n2, m))

print('==========================================================')
print('Outra lógica de resolver o mesmo problema')

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1+n2)/2
print('A média entre {:.1f} e {:.1f} é igual: {:.1f}'.format(n1, n2, m))


