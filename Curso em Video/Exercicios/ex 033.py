#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
#Entrada de dados 
num1 = int(input("Primeiro valor : "))
num2 = int(input("Segundo valor : "))
num3 = int(input("Terceiro valor : "))
menor = num1
maior = num1

#Processamento 
#Verificando quem é o menor 
if num2 < num1 and num2 < num3:
    menor = num2
elif num3 < num1 and num3 < num2:
    menor = num3
#Verificando quem é o maior
if num2 > num1 and num2 > num3:
    maior = num2
elif num3 > num1 and num3 > num2:
    maior = num3
#Saida de dados
print("O menor numero valor digitado foi {}".format(menor))
print("O maior numero valor diditado foi {}".format(maior))