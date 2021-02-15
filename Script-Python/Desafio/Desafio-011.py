# Faça um programa que leia a largura e a altura de uma parada em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2.
# 1 litro pinta 2m2.

a = float(input('Qual é a altura da parede em metros que se deseja pintar: '))
l = float(input('Qual é a largura da parede em metros que se deseja pintar: '))
ar = a * l
t = ar / 2
print('Precisará de {:.1f}l (litros) de tinta.' .format(t))
