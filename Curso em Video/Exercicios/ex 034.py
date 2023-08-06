#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
#Entrada de dados 
salario = float(input("Digite o seu salário do funcionário  para descobrir o aumento : "))
aumento = 0
#Processamento 
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:  
    aumento = salario + (salario * 10 / 100)

#Saida de dados
print("O valor do salário do funcionário R${:.2f}\nO valor do salário com aumento R${:.2f}".format(salario, aumento))