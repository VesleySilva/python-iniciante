#Author: Vesley Cesar da Silva
#Data: 24/11/2021
#Faça um algoritmo que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('=== PROGRAMA EXECUTADO ===')
km = float(input('Digite a quantidade de Km percorrido pelo o carro: '))
qtd = int(input('Digite a quantidades de dia que o carro foi alugado: '))
preco = (km * 0.15) + (qtd * 60)
print('Você alugou o carro por {} dias e andou um total de {} km você deverá pagar um total de R$: {:.2f}'.format(qtd, km, preco))