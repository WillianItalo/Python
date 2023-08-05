#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
#Entrada de dados 
distancia = float(input("Qual é a distância da sua viagem ? : "))
print("Você está prestes a começar uma viagem de {}Km.")

#Processamento 
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

'''if line : preco =  distância * 0.50 if distância <= 200 else distância * 0.45 '''
#Saida de dados
print("O preço da passagem será R${:.2f}".format(preco)) 