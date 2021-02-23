# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.
distancia = int(input('Qual a distância em KM da viagem? '))
if distancia <= 200:
    print('O valor da viagem de {} KM é de R$ {:.2f}'.format(distancia, (distancia*0.50)))
else:
    print('O valor da viagem de {} Km é de R$ {:.2f} .' .format(distancia, (distancia*0.45)))
