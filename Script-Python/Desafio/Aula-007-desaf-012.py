# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual é o preço da mercadoria: R$'))
pd = p * 0.95
print('O preço com desconto fica em R${:.2f} .' .format(pd))
