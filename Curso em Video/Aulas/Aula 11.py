#Veja como utilizar o código \033[m com todas as suas principais possibilidades.
a = ("Um belo momento para ler um livro\n")
b = ("Ou sair para atividades ao ar livre")
cores = {"limpa":"\033[m", 
         "azul":"\033[34m",
         "verde":"\033[32m",
         "preto&branco":"\033[7;30m"}

print("\033[1;31;43mOlá, Mundo!\033[m")
print("\033[4;32;45mQue dia Lindo !\033[m")

print("{}{}{}{}".format(cores["azul"], a, cores["verde"], b))

print("\033[4;36mAproveite seu dia !\033[m")