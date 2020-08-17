import PySimpleGUI as sg
from random import randint

MAX_ROWS = MAX_COL = 10
board = [[randint(0,1) for j in range(MAX_COL)] for i in range(MAX_ROWS)]

layout =  [[sg.Button('',size=(2, 2), key=(i,j), pad=(0,0), button_color=('white','black')) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
layout.append([sg.Button('A', key=(11,1),button_color=('white','black'),size=(2,2)), sg.Button('B', key=(11,2),button_color=('white','black'),size=(2,2)), sg.Button('C', key=(11,3),button_color=('white','black'),size=(2,2)),sg.Button('D', key=(11,4),button_color=('white','black'),size=(2,2)),sg.Button('E', key=(11,5),button_color=('white','black'),size=(2,2))])

atril = [(11,1), (11,2), (11,3), (11,4), (11,5)]
valido = []
for i in range(6):
	for j in range(6):
		tupla = (i,j)
		valido.append(tupla)
		print(valido)

window = sg.Window('Tablero').Layout(layout).Finalize()
inicio = False
sg.Popup('La primera letra debe ir en el casillero del centro')
while True:
	event, values = window.Read()
	if event is None:
		break
	elif event in atril:
		valor_Atril = window.Element(event).GetText()
		letra_selec = event
		if not inicio:
			event, values = window.Read()
			valor_tablero = window.Element(event).GetText()
			if event not in atril:
				if event in valido:
					inicio = True
					if valor_tablero == '':
						tup = event
						window.Element(event).Update(valor_Atril, button_color=('black','pink'))
						window.Element(letra_selec).Update(visible=False)
				else:
					sg.Popup('Debe colocar las letras en consecutivo')
			else:

				window.Element(letra_selec).Update(valor_tablero)
				window.Element(event).Update(valor_Atril)
		else:
			i=tup[0]
			j=tup[1]
			tup=(i,j+1)
			window.Element(tup).Update(valor_Atril, button_color=('black','pink'))
			window.Element(letra_selec).Update(visible=False)
window.Close()
