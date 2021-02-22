# Escreva um programa que leia a velocidade de um carro.
# se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

carro = int(input('Qual a velocidade do carro? '))
print('--=--'*10)
if carro <= 80:
    print('Boa viagem.Continue respeitando o limite de velocidade.')
else:
    multa = 7 * (carro - 80)
    print('MULTADO! Você excedeu o limite permitido que é de 80 Km/h.')
    print('Você deve pagar uma multa de R$ {:.2f}.'.format(multa))
print('--=--'*10)
