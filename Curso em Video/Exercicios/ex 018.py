#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#Entrada de dados
import math 
an = float(input("Digite o ângulo que deseja : "))


#Processamento 
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tan = math.tan(math.radians(an))

#Saida de dados
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cosseno))
print('O ângulo da {} tem a TANGENTE de {:.2f}'.format(an, tan))