#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#Entrada de dados 
from math import trunc
num = float(input('Digite um valor: ' ))

#Processamento 

#Saida de dados
print('O valor Digitado foi {} e a sua parte inteira é {}'.format(num, trunc(num)))