# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.

n = float(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** 0.5
print('O dobro do número escolhido é {:.0f}, o triplo é {:.0f} a sua raiz quadrada é {:.2f} .'. format(d, t, r))
