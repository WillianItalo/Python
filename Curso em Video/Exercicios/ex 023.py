#Faça um programa que leia um número de 0 a 9999 e motre na tela cada um dos dígitos separados. 
#Entrada de dados 
num = int(input("Digite um numero : "))

#Processamento 
u = num // 1 % 10
d = num // 10 % 10 
c = num // 100 % 10 
m = num // 1000 % 10

#Saida de dados
print("Analisando o número {}".format(num))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))