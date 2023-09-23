#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte  o  valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal, não pode execer 30% do salário ou então o emprestimo será negado.

#Entrada de dados 
print("---" * 12)
valcasa = float(input("Digite o valor da casa : "))
salario = float(input("Digite o seu salário : "))
parcelas = int(input("Em quantas parcelas deseja "))

#Processamento 

valoraprovado = salario - (salario * 30 / 100)

#Saida de dados