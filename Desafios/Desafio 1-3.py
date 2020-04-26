# DESAFIO REPETIÇÃO
# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
# qual numero voce deseja receber a sequencia fibonacci? 34

def fib(slast, last, iterat):
	if iterat < 1:
		print("1")
	if iterat-1 == 0:
		result = slast + last
		print(result)
	else:
		fib(last, slast+last, iterat-1)


def start():
	flag = True
	while(flag == True):
		iterations = input("Você deseja o valor de qual iteração da sequência?\n")
		if(int(iterations) < 1):
			print("Por favor insira um valor válido!\n")
		else:
			flag = False
	fib(1,1, int(iterations)-2)
start()
