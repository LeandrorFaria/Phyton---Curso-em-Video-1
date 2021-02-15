# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possiveis sobre eles.

a = input("Digite algo: ")
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('è alfanúmerico?', a.isalnum())
print('Está em minusculas?', a.islower())
print('Está em maiúsculas?', a.isupper())
