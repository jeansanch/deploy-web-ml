# DESAFIO FUNÇÕES
# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverse(input):
	reverse = ""
	size = len(input)
	for x in input:
		reverse = x+reverse
	print(reverse)

def start():
	flag = True
	while(flag == True):
		inp = input("Que valor deseja inverter?\n")
		if(inp.isdigit()):
				flag = False
		else:
			print("Por favor insira um valor válido!\n")
	reverse(inp)
start()