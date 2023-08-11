#Aula 12 IF , Elif & Else.
#Entrada de dados 
nome = str(input("Qual o seu nome ? : \n"))
cores = {"azul": "\033[4;30;44m"}
#Processamento 
if nome == "Joao" or  nome == "Maria" or nome == "Lucas":
    print("Seu nome é populr no Brasil !")
elif nome == "Marcus" or nome == "Ana":
    print("Um nome comum")
elif nome == "Rose":
    print("Que nome lindo ! ")
else:
    print("Seu nome é bem normal.")

#Saida de dados
print("Tenha um ótimo dia, {}{}!".format(cores[azul], nome))