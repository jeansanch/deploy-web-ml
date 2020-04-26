# DESAFIO CONDICIONAIS
# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def turno():
	turno = input("Por favor insira o tuno em que estuda\nUse (M para matutino | V para vespertino ou | N para Noturno\n)")
	turno.upper();
	if turno == "M":
		print("\nBom dia")
	elif turno == "V":
		print("\nBoa tarde")
	elif turno == "N":
		print("\nBoa noite")
	else:
		print("\nValor inválido!")
		
turno()