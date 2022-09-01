from random import randrange


def print_game(values_dict):
	print("----------")
	print("| {} | {} | {} |".format(values_dict['7'], values_dict['8'], values_dict['9']))	
	print("----------")
	print("| {} | {} | {} |".format(values_dict['4'], values_dict['5'], values_dict['6']))
	print("----------")
	print("| {} | {} | {} |".format(values_dict['1'], values_dict['2'], values_dict['3']))
	print("----------")


def check_win(values_dict):
	if (values_dict['1'] == values_dict['2'] == values_dict['3'] != '' or 
	   values_dict['4'] == values_dict['5'] == values_dict['6'] != '' or 
	   values_dict['7'] == values_dict['8'] == values_dict['9'] != '' or
	   values_dict['1'] == values_dict['4'] == values_dict['7'] != '' or 
	   values_dict['2'] == values_dict['5'] == values_dict['8'] != '' or 
	   values_dict['3'] == values_dict['6'] == values_dict['9'] != '' or
	   values_dict['7'] == values_dict['5'] == values_dict['3'] != '' or 
	   values_dict['9'] == values_dict['5'] == values_dict['1'] != ''):  
		return True


def jogo():

	simbolo = 'X'
	contador = 0

	for i in range(10):

		print_game(values_dict)

		print("Vez das {} jogarem! Qual quadrante você escolhe?".format(simbolo))
		quadrante = input()

		if values_dict[quadrante] == '':
			values_dict[quadrante] = simbolo
		else:
			print("O movimento não é valido... Escolha outro quadrante!")
			continue
		
		if check_win(values_dict):
			print("Parabéns {}, você ganhou!".format(simbolo))
			return 0
		else:
			if simbolo == 'X':
				simbolo = 'O'
			else:
				simbolo = 'X'

	print("Opa! Deu velha!")

values_dict = {'1':'', '2':'', '3':'', '4':'', '5':'', '6':'', '7':'', '8':'', '9':''}

jogo()



