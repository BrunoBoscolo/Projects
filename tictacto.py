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
	if (values_dict['1'] == values_dict['2'] == values_dict['3'] or 
	   values_dict['4'] == values_dict['5'] == values_dict['6'] or 
	   values_dict['7'] == values_dict['8'] == values_dict['9'] or
	   values_dict['1'] == values_dict['4'] == values_dict['7'] or 
	   values_dict['2'] == values_dict['5'] == values_dict['8'] or 
	   values_dict['3'] == values_dict['6'] == values_dict['9'] or
	   values_dict['7'] == values_dict['5'] == values_dict['3'] or 
	   values_dict['9'] == values_dict['5'] == values_dict['1']):  
		return True


def play_round(player, values_dict):
	if player == 1:
		quadrante = input("Jogador 1, selecione o quadrante desejado... ")
		values_dict[quadrante] = "O"
		if check_win(values_dict):
			print("Jogador 1 venceu!")

	else:
		quadrante = input("Jogador 2, selecione o quadrante desejado... ") 
		values_dict[quadrante] = "X"
		if check_win(values_dict):
			print("Jogador 2 venceu!")

	print_game(values_dict)	


values_dict = {'1':None, '2':None, '3':None, '4':None, '5':None, '6':None, '7':None, '8':None, '9':None}

for x in range(10):
	if x % 2 == 0:
		play_round(1, values_dict)
	else:
		play_round(0, values_dict)



