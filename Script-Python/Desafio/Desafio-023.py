# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# exemplo digite um número: 1834
# unidade: 4
# dezena:  3
# centena: 8
# milhar:  1

numero = int(input('Digite um número entre 0 e 9999:'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o número {} .' ,format(numero))
print('A unidade de {} é {} .' .format(numero, u))
print('A dezena de {} é {} .' .format(numero, d))
print('A centena de {} é {} .' .format(numero, c))
print('A milhar de {} é {} .' .format(numero, m))
