# Crie um programa que leia o nome completo de uma pessoa e mostra:
# -> O nome com todas as letras maisculas.
# -> O nome com todas as letras minusculas.
# -> Quantas letras ao todos sem considerar espaços
# -> Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo:')
nome = nome.strip()
print(nome.upper())
print(nome.lower())


