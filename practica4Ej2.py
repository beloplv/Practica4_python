import PySimpleGUI as sg
import json
from os.path import isfile

jugadores = {'fede': {'nivel':3,'puntaje':4,'tiempo':200},
    'belen': {'nivel':4,'puntaje':6,'tiempo':300},
    'juan': {'nivel':5,'puntaje':7,'tiempo':400}}

nombre_archivo = 'jugadores.json'

def guardar_datos(nombre_archivo,jugadores):
    with open(nombre_archivo, 'w') as f:
        json.dump(jugadores,f)

def extraer_jugadores(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        jugadores = json.load(f)
    return jugadores

def actualizar_listado (listbox,lista):
     listbox.Update(map(lambda x: "{} - {} - {} - {}".format(x[0],x[1],x[2],x[3]),lista))


def modificoDatos(nombre_archivo):
    if isfile (nombre_archivo):
        datos=extraer_jugadores(nombre_archivo)
        datos[values['nombre']]={'nivel': int(values['nivel']),'puntaje': int(values['puntaje']), 'tiempo': int(values['tiempo'])}
    else:
        datos={}
        datos[nombre]={'nivel': int(nivel),'puntaje': int(puntaje), 'tiempo': int(tiempo)}
    guardar_datos(nombre_archivo,datos)

layout = [[sg.Text('Nombre: '), sg.Input(key='nombre')],[sg.Text('Nivel: '), sg.Input(key='nivel')],
[sg.Text('Puntaje: '), sg.Input(key='puntaje')],[sg.Text('Tiempo: '),sg.Input(key='tiempo')],
[sg.Listbox(values=[], key='Datos', size=(60,10))],[sg.Button('Añadir')]]

window = sg.Window('Datos de jugador').Layout(layout)
window.Finalize()
lista = []

while True:
    event,values = window.Read()
    if event is None:
        break
    if event is 'Añadir':
        lista.append((values['nombre'], values['nivel'], values['puntaje'],values['tiempo']))
        actualizar_listado(window.FindElement('Datos'),lista)
        modificoDatos(nombre_archivo)
        sg.Popup('Se agrego la modificacion')
window.Close()
