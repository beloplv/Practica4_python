import csv
import PySimpleGUI as sg

def contar(archivo):
    leo_archivo = csv.reader(archivo)
    dic = {}
    for fila in leo_archivo:
        if fila[2] != 'Institución' and fila[10] != 'Estudiantes Mujeres':
            if fila[10] != '':
                if fila[2] in dic:
                    dic[fila[2]] = (dic[fila[2]] + int(fila[10]))
                else:
                    dic[fila[2]] = int(fila[10])
    return dic

def actualizar_listado (listbox,lista):
     listbox.Update(map(lambda x: "{}: {}".format(x[0],x[1]),lista))


colum1 = [[sg.Text('Archivo'),sg.Input(),sg.FileBrowse('Buscar archivo', key='_file1_')],
          [sg.Button('Ok')],
          [sg.Button('Ordenar', visible=False, key='Ordeno')]]

colum2 = [[sg.Listbox(values=[], key='Lista_uni', size=(60,10))]]

layout = [[sg.Column(colum1),sg.Column(colum2)],
          [sg.Graph(canvas_size=(1030,400),graph_bottom_left=(-40,-10),graph_top_right=(925,380),background_color='black',key='graph')],
          [sg.Button('Exit')]]

window = sg.Window('Universidades').Layout(layout).Finalize()

lista = []

while True:
    event,values = window.Read()
    if event is None or event == 'Exit':
        break
    elif event == 'Ok':
        if values['_file1_'] == '':
            sg.Popup('Error. No seleccionó ningún archivo')
        else:
            window.FindElement('Ordeno').Update(visible=True)
    elif event == 'Ordeno':
        archivo = open('mujeresEnCarrera.csv','r')
        dic_ord = sorted(contar(archivo).items(), key=lambda uni: uni[1])
        actualizar_listado(window.FindElement('Lista_uni'), dic_ord )
        archivo.close()

        #Gráfico
        graph = window.FindElement('graph')

        graph.DrawLine((0,0),(1000,0))
        graph.DrawLine((0,0),(0,370))

        cont = 0
        for x in range(0,1000,int(1000/85)):
            graph.DrawLine((x,-1),(x,1))
            if x != 0 and cont <= len(dic_ord)-1:
                aux = dic_ord[cont][0].split(' ')
                sigla = ''
                for i in aux:
                    if i != '':
                        sigla = sigla + i[0]
                graph.DrawText(sigla,(x,(dic_ord[cont][1]/20)+10),color='white')
                graph.DrawRectangle(top_left=(x,dic_ord[cont][1]/20), bottom_right=(x+6,0), fill_color='red')
            cont = cont +1
        for y in range(0, 370, 20):
            graph.DrawLine((-3,y),(3,y))
            if y != 0:
                graph.DrawText(y*20, (-20,y), color='white')

window.Close()
