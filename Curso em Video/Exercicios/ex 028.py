#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
#Entrada de dados 
from random import randint 
from time import sleep
computador = randint(0,5) # Faz o computador "PENSAR"

#Processamento 
print("--" * 10)
print("Vou pensar em um número entre 0 e 5.\nTente adivinhar... ")
print("--" * 10)
jogador = int(input("Em que número eu pensei ? ")) #Jogador tenta adivinhar
print("PROCESSANDO...")
sleep(3)
#Saida de dados
if jogador == computador:
    print("Parabéns ! Você conseguiu me vencer! ")
else:
    print("Ganhei ! Eu pensei no número {} e não no número {}!".format(computador,jogador))