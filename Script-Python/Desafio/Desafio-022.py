# Crie um programa que leia o nome completo de uma pessoa e mostra:
# -> O nome com todas as letras maisculas.
# -> O nome com todas as letras minusculas.
# -> Quantas letras ao todos sem considerar espaços
# -> Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome ...')
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.' .format(len(nome)-nome.count(' ')))
print('Seu nome tem {} letras.' .format(nome.find(' ')))
separa = nome.split()
print('Seu nome {} e tem {} letras.'.format(separa[0], len(separa[0])))
