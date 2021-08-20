# buscar_precios.py
import csv
import sys


def cambiarFloat(num):
    try:
        return float(num)
    except ValueError:
        return 0


def costo_camion(archivo):
    try:
        with open(archivo, 'r', encoding='UTF-8') as file:
            rows = csv.reader(file)
            precioTotal = 0
            for row in rows:
                cajones = cambiarFloat(row[1])
                precio = cambiarFloat(row[2])
                precioTotal += cajones * precio
            return round(precioTotal, 2)
    except EnvironmentError:
        print('El Archivo no Existe')


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print(costo)