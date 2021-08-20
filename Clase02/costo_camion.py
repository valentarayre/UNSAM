# costo_camion.py
import csv


def cambiarFloat(num):
    try:
        return float(num)
    except ValueError:
        return 0


def costo_camion(archivo):
    with open(archivo, 'r', encoding='UTF-8') as file:
        rows = csv.reader(file)
        precioTotal = 0
        for row in rows:
            cajones = cambiarFloat(row[1])
            precio = cambiarFloat(row[2])
            precioTotal += cajones * precio
        return round(precioTotal, 2)


costo = costo_camion('../Data/camion.csv')
print(costo)