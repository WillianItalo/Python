#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
#Entrada de dados 
print("--" * 20)
num = int(input("Digite um número, para descobrir se é Par ou Impar : "))
resultado = num % 2
#Processamento 
if resultado == 0:
    print("Número digitado {} é 'PAR' ".format(num))
else:
    print("Número digitado {} é 'ÍMPAR' ".format(num))
#Saida de dados
print("Fim")
print("--" * 20)
