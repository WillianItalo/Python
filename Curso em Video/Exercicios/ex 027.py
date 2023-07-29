#Crie um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 
#Entrada de dados 
n = str(input("Digite seu nome completo: ")).upper().strip()

#Processamento 
nome = n.split()

#Saida de dados
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format(nome[0]))
print("Seu último nome é {}".format(nome[len(nome)-1]))