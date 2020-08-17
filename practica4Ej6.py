import PySimpleGUI as sg
import random
import json

def abrircoordenadas(filename):
    lista_coordenadas_x = []
    lista_coordenadas_y = []
    with open(filename,'r') as file:
        datos = file.readlines()
        for coor in datos:
            coor=coor.replace("(","").replace("),","").replace("[","").replace(")]","")
            x,y=coor.split(",")
            lista_coordenadas_x.append(int(x))
            lista_coordenadas_y.append(int(y))
    return ([lista_coordenadas_x,lista_coordenadas_y])

def ziprandom(lis1,lis2):
    random.shuffle(lis2)
    return zip(lis1,lis2)

def abrircolores(filename):
    lista_colores=[]
    with open (filename,'r') as file:
        datos=file.readlines()
        for color in datos:
            color=color.replace("[","").replace("]","").replace("\n","").replace(",","").replace('"',"")
            lista_colores.append(color)
    return lista_colores

def dibujarGrafico(window, cor, color):
    grafico = window.FindElement('_graph_')
    strCorX =str(cor[0]).replace('[','').replace(']','')
    strCorY = str(cor[1]).replace('[','').replace(']','')
    coordenada = ((int(strCorX),int(strCorY)))
    grafico.DrawPoint(coordenada,5,color[0])

def actualizar_listado(listbox,lista):
    listbox.Update(map(lambda x :'Coordenadas {} | Colores {}'.format(x[0],x[1]),lista))

def guardar_datos(lista):
    with open ('datos2.json','w') as file:
        json.dump(lista,file)

coord = abrircoordenadas('coordenadas.json')

layout = [[sg.Text('Bienvenido')],
          [sg.Text('Color'),sg.Listbox(values = abrircolores('colores.json'), key ='Colores')],
          [sg.Text('Coordenadas'), sg.Text('              '), sg.Text('lista'),sg.Listbox(values = [], key ='Datos', size = (40,1))],
          [sg.Text('X'),sg.Listbox(values = coord[0], key ='CoorX'), sg.Text('Y'),sg.Listbox(values = coord[1], key ='CoorY')],
          [sg.Graph(canvas_size=(400,400), graph_bottom_left=(-105,-105), graph_top_right=(105,105),key='_graph_')],
          [sg.Button('dibujar'),sg.Button('añadir'),sg.Button('guardar'), sg.Exit()]]

window = sg.Window('Window that stays open').Layout(layout).Finalize()
graph = window.FindElement('_graph_')
lista=[]
# Draw axis
graph.DrawLine((-100,0), (100,0))
graph.DrawLine((0,-100), (0,100))

for x in range(-100, 101, 20):
    graph.DrawLine((x,-3), (x,3))
    if x != 0:
        graph.DrawText( x, (x,-10), color='green')

for y in range(-100, 101, 20):
    graph.DrawLine((-3,y), (3,y))
    if y != 0:
        graph.DrawText( y, (-10,y), color='blue')

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    elif event == 'dibujar':
        if values['CoorX'] == [] or values['CoorY'] == [] or values['Colores'] == []:
            sg.Popup("Error falta seleccionar algun dato")
        else:
            dibujarGrafico(window,(values['CoorX'],values['CoorY']),values['Colores'])
    elif event == 'añadir':
            cor = (values['CoorX'][0],values['CoorY'][0])
            lista.append((cor,values['Colores'][0]))
            actualizar_listado(window.FindElement('Datos'),lista)
    elif event == 'guardar':
        guardar_datos(lista)
        sg.Popup('Los datos se guardaron exitosamente')

window.Close()
