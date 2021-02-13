# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por KM rodado.
# dia custa R$ 60
# km rodado R$ 0.15

dia = int(input('Quantos dias alugado? '))
km = int(input('Quantos Km rodados? '))
vld = dia * 60
vlkm = km * 0.15
pago = vld + vlkm
print('Por ter usado o carro por {} dias e percorrigo {} km, o valor a pagar é de R$ {:.2f}.' .format(dia, km, pago))
