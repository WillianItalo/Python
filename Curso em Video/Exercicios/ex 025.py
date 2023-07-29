#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
#Entrada de dados 
nome = str(input("Digite o seu nome completo : ")).strip()

#Processamento 
 
#Saida de dados
print("Seu nome tem Silva? {}".format("silva" in nome.lower()))