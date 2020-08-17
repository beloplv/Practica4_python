import PySimpleGUI as sg
import random
import json

dic_datos={}

def abrircoordenadas(filename):
    lista_coordenadas = []
    with open(filename,'r') as file:
        datos = file.readlines()
        for coor in datos:
            coor=coor.replace("(","").replace("),","").replace("[","").replace(")]","")
            x,y=coor.split(",")
            lista_coordenadas.append((int(x),int(y)))
    return lista_coordenadas

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

def dibujarGrafico(window, coord, col):
    coordenadas = abrircoordenadas(coord)
    colores = abrircolores(col)
    grafico = window.FindElement('_graph_')
    for coord,col in ziprandom(coordenadas,colores):
        dic_datos[str(coord)]=col
        grafico.DrawPoint(coord,5,col) # 5 significa el tamaño del punto

def guardar_datos(dic_datos):
    with open ('datos.json','w') as file:
        json.dump(dic_datos,file)


layout = [[sg.Text('Buscar archivo')],
          [sg.FileBrowse('Buscar coordenadas...', key='_file1_'), sg.Button('coord')],
          [sg.FileBrowse('Buscar colores...', key='_file2_'), sg.Button('color')],
          [sg.Graph(canvas_size=(400,400), graph_bottom_left=(-105,-105), graph_top_right=(105,105),key='_graph_')],
          [sg.Button('dibujar'),sg.Button('guardar'), sg.Exit()]]

window = sg.Window('Window that stays open').Layout(layout).Finalize()

graph = window.FindElement('_graph_')

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
    elif event == 'coord':
        sg.Popup('Abriendo archivo de coordenadas')
        if values['_file1_'] == '':
            sg.Popup('No cargaste el archivo')
        else:
            abrircoordenadas(values['_file1_'])
    elif event == 'color':
        sg.Popup('Abriendo archivo de colores')
        if values['_file2_'] == '':
            sg.Popup('No cargaste el archivo')
        else:
            abrircolores(values['_file2_'])
    elif event == 'dibujar':
        if values['_file1_'] == '' or values['_file2_'] == '':
            sg.Popup('No cargaste los archivos')
        else:
            dibujarGrafico(window,values['_file1_'],values['_file2_'])
    elif event == 'guardar':
        guardar_datos(dic_datos)
        sg.Popup('Los datos se guardaron exitosamente')


window.Close()
