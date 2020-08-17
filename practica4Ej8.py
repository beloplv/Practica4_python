import PySimpleGUI as sg
import csv

archivo=open('universidades.csv','r')
dic={}

lista=[]

def datos(archivo):
    dic={}
    leo=csv.reader(archivo)
    for fil in leo:
        fila=str(fil)
        fila=fila.replace("[","").replace("]","").replace('"',"").split(";")
        if fila[1] != 'UNIVERSIDA':
            if not fila[1] in lista:
                lista.append(fila[1])
            datos1={fila[3]:{'REGIMEN':fila[0],'UNAC_C':fila[4],'ANEXO_C':fila[5],'UNICUE':fila[6],'CUI':fila[7],'TELEFONO':fila[8],'FAX':fila[9],'WEB':fila[10],'DIRECCION':fila[11],'WKT_GKBA':fila[14],'BARRIO':fila[15],'COMUNA':fila[16],'CODIGO POSTAL':fila[17],'CODIGO POSTAL ARGENTINO':fila[18],'LAT':fila[19],'LNG':fila[20]}}
            if fila[1] in dic:
                dic[fila[1]].update(datos1)
            else:
                dic[fila[1]]=datos1
    return dic

diccionario=datos(archivo)

layout =[[sg.Listbox(values=lista,key='uni',size=(60,1))],[sg.Button('Ver info')],
        [sg.Listbox(values=[],key='listado',size=(60,20))],
        [sg.Button('Exit')]]

window = sg.Window('Universidades').Layout(layout).Finalize()

while True:
    event,values=window.Read()
    if event is None or event == 'Exit':
        break
    elif event == 'Ver info':
        lis=str(diccionario[values['uni'][0]])
        lis=lis.replace("{","").replace('}',"").replace("'","").split(",")
        window.FindElement('listado').Update(lis)
window.Close()
