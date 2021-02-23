# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('--=--' * 7)
print('Analisador de triângulo')
print('--=--' * 7)
a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos informados pode FORMAR um triângulo!')
else:
    print('Os segmentos não podem formar um triângulo!')