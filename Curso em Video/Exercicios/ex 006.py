#Crie um algoritimo que que leia um número, mostre o seu dobro, triplo e raiz quadrada.
#Entrada de dados 
n = int(input('Digite um número: '))

#Processamento 
d = n * 2 
t = n * 3
r = n ** (1/2)

#Saida de dados
print('O dobro de {} vale : {}'.format(n, d))
print('O triplo de {} vale : {}'.format(n, t))
print('A raiz quadradada de {} é : {:.2f}'.format(n, r))
