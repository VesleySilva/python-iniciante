#Author: Vesley Cesar da Silva
#Data: 24/11/2021
# 08 - Escreva um programa que lê um valor em metros e exiba ele convertido em centímetros e milímetros

print('=== PROGRAMA EXECUTADO ===')
metro = float(input('Digite um valor em metros: '))
centimetros = metro * 100
milimetros = metro * 1000

print('O metro digitado foi de: {:.1f} convertido para centimetros: {:.1f}'.format(metro, centimetros))
print('O metro digitado foi de: {:.1f} convertido para milimetros: {:.1f}'.format(metro, milimetros))

print('==========================================================')
print('Outra lógica de resolver o mesmo problema')

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print(' A medida de metros corresponde: {:.1f} \n A de centímetros corresponde: {:.1f} \n A de milímetros corresponde: {:.1f}'.format(medida, cm, mm))

print('=' * 58)

#Programa que converta metros em:
#Decâmetro (dam)
#Hectômetro (hm)
#Quilômetro (km)
#Decímetro (dm)
#Centímetro (cm)
#Milímetro (mm)

m = float(input('Digite uma distância em metros: '))
dam = m / 10
hm = m / 100
km = m / 1000
dm = m * 10
cm = m * 100
mm = m * 1000

print('{} metros corresponde a: {} Decâmetro'.format(m, dam))
print('{} metros corresponde a: {} Hectômetro'.format(m, hm))
print('{} metros corresponde a: {} Quilômetro'.format(m, km))
print('{} metros corresponde a: {} Decímetro'.format(m, dm))
print('{} metros corresponde a: {} Centímetros'.format(m, cm))
print('{} metros corresponde a: {} Milímetros'.format(m, mm))

