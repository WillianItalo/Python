#Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessário para pinta-lá , sabendo que cada litro de tinta, pinta uma área de 2m²
#Entrada de dados 
lar = float(input('Digite a Largura da parede : '))
alt = float(input('Digite a altura da parede :  '))

#Processamento 
mquad = lar * alt
litr = mquad / 2 

#Saida de dados

print('A parede tem a dimensão de {}X{} e sua área de {}M², será necessário {}L de Tinta, para pintar a parede .'.format(lar, alt, mquad,  litr))