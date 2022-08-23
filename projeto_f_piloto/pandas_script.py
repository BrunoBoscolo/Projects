import pandas as pd
#import matplotlib.pyplot as plt
#from tkinter import *

#root = Tk()

#canvas = Canvas(root, width=500, height=500)
#canvas.grid(column=0, row=0, sticky=(N, W, E, S))

#plt.figure()

#ax = plt.axes(projection="3d")

df1 = pd.read_excel('projeto_piloto/static/data/data_pressao.xlsx', sheet_name=0, header=None)

df2 = pd.read_excel('projeto_piloto/static/data/data_pressao.xlsx', sheet_name=1, header=None)

list_profile = []

list_pie_e_x = []
list_pie_e_y = []

list_pie_d_x = []
list_pie_d_y = []

list_pression_e = []
list_pression_d = []

list_tiempo = []


list_profile.append(df1.iloc[0][1])
list_profile.append(df1.iloc[1][1])
list_profile.append(df1.iloc[2][1])
list_profile.append(df1.iloc[3][1])
list_profile.append(df1.iloc[4][1])
list_profile.append(df1.iloc[5][1])
list_profile.append(df1.iloc[6][1])
list_profile.append(df1.iloc[7][1])

#print(list_profile)

for x in range(17, 256):
	list_tiempo.append(df2.iloc[x][1])

#print(list_tiempo)

for x in range(16, 95):
	list_pie_e_x.append(df1.iloc[x][1])
	list_pie_e_y.append(df1.iloc[x][2])

for x in range(96, 140):
	list_pie_e_x.append(df1.iloc[x][5])
	list_pie_e_y.append(df1.iloc[x][6])

for x in range(16, 140):
	list_pie_d_x.append(df1.iloc[x][3])
	list_pie_d_y.append(df1.iloc[x][4])	

#print(list_pie_e_x)	

#print(list_pie_e_y)	

#print(list_pie_d_x)	

#print(list_pie_d_y)	
for x in range(len(list_tiempo)):
	print("------------------------------")
	print("Tempo = {} \n Posição esquerdo = ({},{}) \n Posição direito = ({},{})".format(list_tiempo[x], list_pie_e_x[x], list_pie_e_y[x], list_pie_d_x[x], list_pie_d_y[x],))
	print("------------------------------")

#print(len(list_tiempo))
#print(len(list_pie_e_x))
#print(len(list_pie_e_y))
#print(len(list_pie_d_x))
#print(len(list_pie_d_y))

	#for x in range(len(list_x)):
	#	canvas.create_line(abs(list_x[x]), abs(list_y[x]), abs(list_x[x]), abs(list_y[x])-5, fill='red', width=10)

#list_x = dfp["pie_e_x"].tolist()
#list_y = dfp["pie_e_y"].tolist()
#plt.plot(dfp["pie_e_x"].tolist(), dfp["pie_e_y"].tolist(), 'o')

#plt.show()

#root.mainloop()

#with pd.option_context('display.max_rows', None,'display.max_columns', None,'display.precision', 3):

	#print(dfp)