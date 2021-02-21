# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = input('Digite o nome de uma cidade:')
cidade = cidade.strip()
cidade = cidade.upper()
print(cidade[:5] =='SANTO')

