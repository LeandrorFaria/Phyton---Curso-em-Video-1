# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos Dólares ela pode comprar
# US$ 1.00 = R$ 3.27

r = float(input('Qual valor de reais que tem na sua carteira: '))
d = r / 3.27
print('Com os reais que possui pode comprar US$ {:.2f} .' .format(d))
