#Author: Vesley Cesar da Silva
#Data: 24/11/2021
# 10 - Crie um programa que lê quantos dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

print('=== PROGRAMA EXECUTADO ===')
dinheiro = float(input('Digite a quantidade de dinheiro em real que você tem R$: '))
dolar = float(input('Digite a cotação do dólar do dia: '))
conversao = dinheiro / dolar
print('Você tem um total na carteira em R$: {:.2f} convertido para US$ : {:.2f}'.format(dinheiro, conversao))

print('=' * 58)
print('Resolvendo mesmo problema com uma lógica diferente, com a dólar valendo UU$ 5,00')
real = float(input('Quantos dinheiro você tem na carteira R$: '))
dolar_con = real / 5.00
print('Com R$: {:.2f} você pode comprar UU$: {:.2f}'.format(real, dolar_con))

print('=' * 58)
#Programa que você digita a quantidade de reais e ele converta para as seguintes moedas:
#Dólar - dl - R$ 5,61
#Euro - eur - R$ 6,28
#Franco Suíco - fs - R$ 6,00
#Iene - ien - 0.049

re = float(input('Digite o valor em real para conversão: R$: '))
print('Com R$: {:.2f} você pode comprar Dólar UU$ : {:.2f}'.format(re, (re / 5.61)))
print('Com R$: {:.2f} você pode comprar Euro ¢ : {:.2f}'.format(re, (re / 6.28)))
print('Com R$: {:.2f} você pode comprar Franco Suíço F : {:.2f}'.format(re, (re / 6.00)))
print('Com R$: {:.2f} você pode comprar Iene Japonês Y : {:.2f}'.format(re, (re * 0.049)))

print('=' * 58)