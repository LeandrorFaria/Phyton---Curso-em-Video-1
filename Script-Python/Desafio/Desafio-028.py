# Escreva um programa que faça o computador "pensar" em número inteiro entre 0 e 5 peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela o se o usuário venceu ou perdeu.
from random import randint

computador = randint(0,5) # computador escolhe um número
print('-=-' *10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar ...')
print('-=-' *10)
jogador = int(input('Em qual número eu pensei?')) # jogador dá seu palpite
print('-=-' *10)
if jogador == computador:
    print('Parabéns!!! Você acertou e venceu.')
else:
    print('Ganhei! Eu pensei no {} e não no {}.'.format(computador, jogador))
print('-=-' *10)