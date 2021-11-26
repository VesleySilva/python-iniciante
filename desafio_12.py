#Author: Vesley Cesar da Silva
#Data: 24/11/2021
# 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

print('=== PROGRAMA EXECUTADO ===')
preco_prod = float(input('Digite o valor do produto: '))
preco_rea = (preco_prod * 0.05)
preco_fin = (preco_prod - preco_rea)
print('Preço antigo do produto era: {:.2f} depois do desconto de 5% ele passou a valer: {:.2f}'.format(preco_prod, preco_fin))

print('=' * 58)
print('Resolvendo o mesmo problema usando uma lógica diferente')
preco = float(input('Qual o preço do produto R$: '))
novo = preco - (preco * 5 / 100)
print('O produto que custava R$: {:.2f} , na promoção com desconto de 5% vai custar R$: {:.2f}'.format(preco, novo))

