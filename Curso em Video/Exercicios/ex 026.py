#Crie um programa que leia uma frase pelo teclado
#Quantas vezes aparec a letra "A" , em que posição ela aparece pela primeira vez , em que posição ela aparece a última vez.
#Entrada de dados 
frase = str(input("Digite uma frase: ")).upper().strip()

#Processamento 
 
#Saida de dados
print("A letra 'A' aparece {} vezes na frase.".format(frase.count("A")))
print("A primeira letra 'A' apareceu na posição {}.".format(frase.find("A")+1))
print("A útilma letra 'A' apareceu na posição {}.".format(frase.rfind("A")+1))
