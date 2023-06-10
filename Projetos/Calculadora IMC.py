# Entrada de dados
nome = input('Digite seu nome   : ')
idade = int(input("Digite sua idade  : "))
altura = float(input("Digite sua altura : "))
peso = float(input("Digite seu peso   : "))

# Processamento
print('{}  |  Idade {}'.format(nome, idade))
imc = float(peso / (altura * altura))
print('Seu IMC é : ',imc)

# Saída de dados
if imc < 17:
	print('Muito abaixo do peso ideal')
elif imc < 18.49:
	print('Abaixo do peso')
elif imc < 24.99:
	print('Peso normal')
elif imc < 34.99:
	print('Obesidade grau 1')
elif imc < 39.99:
	print('Obesidade grau 2')
else:
 print('Obesidade grau 3')