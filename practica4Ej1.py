import PySimpleGUI as sg
import json
import time

###############################################################################

nombre_archivo = 'clima.json'
def guardar_datos(nombre_archivo, datos_guardar):
    d = {}
    dt_string = time.strftime("%a, %d %b %Y %H:%M:%S")
    print('date and time =',dt_string)
    d[dt_string] = datos_guardar
    with open(nombre_archivo, 'w') as f:
        json.dump(d,f)

################################################################################
def actualizar_listado(listbox,lista):
    print(lista)
    listbox.Update(map(lambda x: 'Temperatura {} - Humedad {}'.format(x[0],x[1]),lista))

layout = [[sg.Text('Temperatura:'), sg.Input(key='temperatura')],
          [sg.Text('Humedad:'), sg.Input(key='humedad')],
          [sg.Listbox(values=[], key='Datos', size=(60,10))],
          [sg.Button('Añadir'), sg.Button('Guardar')]]

window = sg.Window('Datos').Layout(layout)
window.Finalize()
lista_cantidades = []

while True:
    event, values = window.Read()
    if event is None:
        break
    if event is 'Añadir':
        lista_cantidades.append((values['temperatura'], values['humedad']))
        actualizar_listado(window.FindElement('Datos'), lista_cantidades)
    if event is 'Guardar':
        print(lista_cantidades)
        guardar_datos(nombre_archivo, lista_cantidades)
