import json
import pattern.es
from pattern.es import conjugate
from pattern.es import INFINITIVE
from collections import Counter

nombre= 'archivo.json'
nombre_archivo= 'verbos.json'
lista1 = []
lista2 = []

def crear(lista1):
        for x in pattern.es.lexicon.keys():
            if x in pattern.es.spelling.keys():
                s=(pattern.es.parse(x).split())
                for cada in s:
                    for c in cada:
                        if (c[1] == 'VB'):
                            lista1.append(x)

def guardar_datos1(nombre, lista1):
     with open(nombre, 'w') as f:
         json.dump(lista1, f)

def cargar_datos1(nombre):
     with open(nombre, 'r') as f:
         lista1 = json.load(f)
     return lista1

################################################################################

def abrir_archivo(lista2):
    with open('archivo.json', 'r') as f:
        arch= json.load(f)
        for x in arch:
            palabra=(conjugate(x, INFINITIVE))
            lista2.append(palabra)

def guardar_datos(nombre_archivo, cnt):
     with open(nombre_archivo, 'w') as f:
         json.dump(cnt, f)

def cargar_datos(nombre_archivo):
     with open(nombre_archivo, 'r') as f:
         cnt = json.load(f)
     return cnt





crear(lista1)
guardar_datos1(nombre,lista1)
cargar_datos1(nombre)
abrir_archivo(lista2)
cnt=Counter (lista2)
guardar_datos(nombre_archivo,cnt)
cargar_datos(nombre_archivo)
