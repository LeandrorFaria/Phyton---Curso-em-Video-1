# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o ângulo que deseja:'))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem SENO de {:.2f} .'.format(angulo, seno))
coss = math.cos(math.radians(angulo))
print('O ângulo de {} tem COSSENO de {:.2f} .' .format(angulo, coss))
tang = math.tan(math.radians(angulo))
print('O ângulo de {} tem TANGENTE de {:.2f} .' .format(angulo, tang))
