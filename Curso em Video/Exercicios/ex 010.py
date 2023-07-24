#Crie um programa que leia quanto dinehiro tem na carteira e mostre quantos Dólares ela pode comprar.
#Entrada de dados 

dolar = 4.80
carteira = float(input('Digite quanto você tem na carteira em R$ ? '))

#Processamento 

d = carteira / dolar

#Saida de dados
 
print('Com R${:2f} você pode comprar ${:2f}'.format(carteira, d))