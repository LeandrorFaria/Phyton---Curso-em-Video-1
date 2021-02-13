# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

m = float(input('Qual é o valor em metros: '))
c = m * 100
mm = m * 1000
print('O valor convertido em centimetros é {:.0f} e o valor convertido em milimitros é {:.0f} .' .format(c, mm))
