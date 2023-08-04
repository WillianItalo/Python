#Entrada de dados 
n1 = float(input("Digite a sua primeira nota : " ))
n2 = float(input("Digite a sua segunda nota : "))


#Processamento 
res = (n1+n2)/2
if res >= 6:
  print("Sua média foi boa Parabéns !!!")
else:
  print("Sua média foi ruim ! Estude mais !! ")

#Saida de dados
print ("Sua média foi {:.1f}".format(res))