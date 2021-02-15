# Faça um programa que leia algo pelo teclado e mostra na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

msg = input('Digite um dado: ')
print('Qual é o tipo de ', msg, ' ?',type(msg))
print(msg, 'é um núemro ? ', msg.isnumeric(), 'ou é letra (alpha) ?', msg.isalpha() )
