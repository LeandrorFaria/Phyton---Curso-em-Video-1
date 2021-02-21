# Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente.
#Exemplo: Ana Maria Braga
# primeiro: Ana
# último: Braga

nome = str(input('Qual seu nome completo: ')).strip()
nome_separado = nome.split()
print('Seu primeiro nome é : {}'.format(nome_separado[0]))
print('Seu último nome é : {}'.format(nome_separado[len(nome_separado) - 1]))

