'''
. Utilizando la solución del ejercicio anterior, se deberá incrementar la
cantidad de caracteres a 7 sobre el tablero B y se deberá intentar formar
una palabra existente, utilizando el módulo pattern, con un mínimo de
2 caracteres y un máximo de 7.
'''
import PySimpleGUI as sg
from pattern.es import spelling,lexicon,parse
from random import randint


tam_celda =25
color_button = ('white','blue')
color_tablero = ('white','red')
tam_button = 5,2
MAX_ROWS = MAX_COL = 10
board = [[randint(0,1) for j in range(MAX_COL)] for i in range(MAX_ROWS)]



layout =  [[sg.Button('',size=(6, 3), key=(i,j), pad=(0,0),button_color = color_tablero) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
layout.append([sg.Button('A', key=(11,1),button_color=color_button,size=tam_button), sg.Button('B', key=(11,2),button_color=color_button,size=tam_button), sg.Button('C', key=(11,3),button_color=color_button,size=tam_button),sg.Button('D', key=(11,4),button_color=color_button,size=tam_button),sg.Button('E', key=(11,5),button_color=color_button,size=tam_button), sg.Button('F', key=(11,6),button_color=color_button,size=tam_button), sg.Button('G', key=(11,7),button_color=color_button,size=tam_button)])
layout.append([sg.Button('Evaluar', key=(13,13),button_color=color_button,size=tam_button)])

botones = {'A' : (11,1),'B' : (11,2),'C' : (11,3),'D' : (11,4),'E' : (11,5),'F' : (11,6),'G' : (11,7)}
guardado ={}
palabra = []
ubicacion = []
window = sg.Window('tablero', default_button_element_size=(5,2), auto_size_buttons=False).Layout(layout).Finalize()

while True:
	event, values = window.Read()
	if event in (None, 'Exit'):
		break
	elif event != (13,13):
		if event in botones.values():
			valor_A = window.Element(event).GetText()
			print(event)
			keys_entered = event
			event, values = window.Read()
			valor_B = window.Element(event).GetText()
			if event not in botones.values():
				if valor_B == '':
					window.Element(event).Update(valor_A, button_color=('white','black'))
					window.Element(keys_entered).Update(text='')
					#palabra.append(valor_A)
					ubicacion.append(event)
					guardado[event] = valor_A
			else:
				window.Element(keys_entered).Update(valor_B)
				window.Element(event).Update(valor_A)
		else:
			print (event)
	else:
		ubicacion = sorted(ubicacion, key=lambda tup: tup[1])
		x= ubicacion[0][0]
		y= ubicacion[0][1]

		incorrecto= False
		for i in range(len(ubicacion)):
			if i != 0:
				if ubicacion[i][0] == x:
					if ubicacion[i][1] == y+1:
						y=y+1
					else:
						incorrecto = True
						break
				else:
					incorrecto = True
					break
		if incorrecto:
			sg.Popup('ubicacion incorrecta vuelva a intentarlo')
			for i in ubicacion:
				window.Element(i).Update('', button_color = color_tablero)
			#ubicacion = []
				window.Element(botones[guardado[i]]).Update(text= guardado[i])
			guardado={}
			ubicacion=[]
			'''
			for i in palabra:
				window[botones[i]].update(text= i)
				#window[i].update(letra[u],button_color=color_button, visible=True)


			palabra =[]
			'''
		else:

			for i in ubicacion:
				palabra.append(guardado[i])

			strPal=''.join(palabra)
			if strPal in spelling.keys() or strPal in lexicon.keys():
				sg.Popup('se ubico la palabra')
				ubicacion = []
				palabra = []
				guardado={}
			else:
				sg.Popup('la palabra no es correcta,vuelva a intentarlo')
				for i in ubicacion:
					window.Element(i).Update('', button_color = color_tablero)
				#ubicacion = []
					window.Element(botones[guardado[i]]).Update(text= guardado[i])
				guardado={}
				ubicacion=[]
				palabra=[]
				'''

				for i in palabra:
					window[botones[i]].update(text = i)
					#window[i].update(letra[u],button_color=color_button, visible=True)


				palabra = []
				'''
window.Close()
