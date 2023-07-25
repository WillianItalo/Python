#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
#Entrada de dados 
catoposto = float(input("Digite o comprimento do cateto oposto : "))
catadjacente = float(input("Digite o comprimento do cateto adjacente : "))

#Processamento 
hi = ( catoposto ** 2 + catadjacente ** 2) ** (1/2)

#Saida de dados
print(" A hipotenusa vai medir {:.2f}".format(hi))

# Importando biblioteca 'math'
# Import math
# catoposto = float(input("Digite o comprimento do cateto oposto : "))
# catadjacente = float(input("Digite o comprimento do cateto adjacente : "))
# hi = math.hypot(catoposto, catadjacente)
# print(" A hipotenusa vai medir {:.2f}".format(hi))