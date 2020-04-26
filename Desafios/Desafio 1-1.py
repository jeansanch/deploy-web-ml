# DESAFIO PYTHON
# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

def ideal():
	flag = True
	while(flag == True):
		height = input("Insira sua altura em centímetros\n");
		if(height.isdigit()):
			flag = False
		else:
			print("Por favor insira um valor válido!\n")
	height = float(height)/100
	idealW = 72.7*height-58
	print("\nSeu peso ideal é: "+str(idealW)+"kg")
ideal()	
