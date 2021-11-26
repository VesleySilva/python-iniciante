#Author: Vesley Cesar da Silva
#Data: 24/11/2021
# 10 - Faça um programa que lê a largura e a altura de uma parede em metros e calcule a sua área e quantidade de tinta necessária para pintá-las abendo que cada litro de tinta pinta uma área de 2m quadrados

print('=== PROGRAMA EXECUTADO ===')
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area_qua = (altura*largura)
pintura = (area_qua / 2)
print('È necessário {:.2f} litros de tinta para cobrir toda a parede'.format(pintura))

print('=' * 58)
print('Resolvendo o mesmo problema usando uma lógica diferente')
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {:.2f} x {:.2f} m² e sua área é de: {:.2f} m²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {:.2f} litros de tinta'.format(tinta))

