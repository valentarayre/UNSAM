# arboles.py
import csv

from collections import Counter


# una lista de diccionarios
def leer_parque(nombre_archivo, parque):
    with open(nombre_archivo, 'r', encoding='UTF-8') as file:
        rows = csv.reader(file)
        encabezados = next(rows)
        lista = []
        for n_fila, fila in enumerate(rows, start=1):
            record = dict(zip(encabezados, fila))
            arbol = {}
            try:
                if parque == record['espacio_ve']:
                    arbol['nombre_com'] = record['nombre_com']
                    arbol['altura_tot'] = float(record['altura_tot'])
                    arbol['inclinacio'] = float(record['inclinacio'])
                    lista.append(arbol)
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        return lista


def especies(lista_arboles):
    especies = []
    for arbol in lista_arboles:
        especies.append(arbol['nombre_com'])
    return set(especies)


def contar_ejemplares(lista_arboles):
    especies = Counter()
    for arbol in lista_arboles:
        nombre = arbol['nombre_com']
        if nombre in especies:
            especies[nombre] += 1
        else:
            especies[nombre] = 1
    return especies


def obtener_alturas(lista_arboles, especie):
    cantidad = 0
    altura_total = 0
    alt_max = 0
    for arbol in lista_arboles:
        nombre = arbol['nombre_com']
        if nombre == especie:
            cantidad += 1
            altura_total += arbol['altura_tot']
            if alt_max < arbol['altura_tot']:
                alt_max = arbol['altura_tot']
    if altura_total > 0:
        promedio = altura_total / cantidad
        return [alt_max,promedio]
    return [0,0]


def obtener_inclinaciones(lista_arboles, especie):
    cantidad = 0
    altura_total = 0
    alt_max = 0
    for arbol in lista_arboles:
        nombre = arbol['nombre_com']
        if nombre == especie:
            print(arbol['inclinacio'])
            cantidad += 1
            altura_total += arbol['inclinacio']
            if alt_max < arbol['inclinacio']:
                alt_max = arbol['inclinacio']
    if altura_total > 0:
        promedio = altura_total / cantidad
        return [alt_max,promedio]
    return [0,0]


parque = "GENERAL PAZ"
especie = 'Jacarandá'

lista_arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parque)
print(parque, len(lista_arboles))

list_especie = especies(lista_arboles)
contar_ejemplares =contar_ejemplares(lista_arboles)
obtener_alturas(lista_arboles, especie)

a =obtener_inclinaciones(lista_arboles, especie)
print(a)
