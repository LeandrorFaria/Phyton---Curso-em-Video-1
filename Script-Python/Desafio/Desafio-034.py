# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual valor atual do salário? '))
if salario >= 1250:
    aumento = salario * 0.15
else :
    aumento = salario * 0.1
novo_salario = salario + aumento
print('O valor do aumento será de R$ {:.2f} e o novo salário ficará em R$ {:.2f}.' .format(aumento, novo_salario))
