#Crie um programa que leia o nome completo de uma pessoa e mostre :
#Nome com todas letras maiuscula , com todas as letras minusculas, quantas letras ao todo, quantas letras tem o primeiro nome 
#Entrada de dados 
nome = input('Digite o seu nome completo  : ').strip()

#Processamento 


#Saida de dados

print('Seu nome em maiúsculas : \n{} '.format(nome.upper()))
print('Seu nome em minúsculas : \n{}'.format(nome.lower()))
print('Seu nome te ao todo {} letras '.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))