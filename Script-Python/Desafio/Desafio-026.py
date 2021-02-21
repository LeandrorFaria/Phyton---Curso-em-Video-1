# Faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra "A"
# em que posição ela aparece a primeira vez.
# em que posição ela aparece da última vez.

frase = str(input('Diga uma frase que te norteia: ')).lower().strip()
print('A letra a aparece {} vezes.' .format(frase.count('a')))
print('A primeira letra a apareceu na posição {} .' .format(frase.find('a')+1))
print('A última letra a apareceu na posição {} .' .format(frase.rfind('a')+1))
