# informe.py
import csv


def leer_camion(ruta):
    with open(ruta, 'r', encoding='UTF-8') as file:
        rows = csv.reader(file)
        lista = []
        for row in rows:
            camion = {}
            if row and row[0] != 'nombre':
                camion['nombre'] = row[0]
                camion['cajones'] = int(row[1])
                camion['precio'] = float(row[2])
                lista.append(camion)
        return lista

def leer_precios(ruta):
    with open(ruta, 'r', encoding='UTF-8') as file:
        rows = csv.reader(file)
        lista = {}
        for row in rows:
            if row:
                lista[row[0]] = float(row[1])
        return lista



camiones = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')

for camion in camiones:
    productoCamion = camion['nombre']
    cantidadCamion = camion['cajones']
    precioCamion = camion['precio']
    costoCamion = round(cantidadCamion * precioCamion, 2)
    if productoCamion in precios:
        ventaCamion = round(precios[productoCamion] * cantidadCamion, 2)
    else:
        print('falta Producto')
    diferenciaCamion = round(ventaCamion - costoCamion, 2)

    if diferenciaCamion > 0:
        balanceCamion = 'Hubo Ganancia'
    else:
        balanceCamion = 'Hubo Perdida'

    print('Producto: {}, Costo del Camion: {}, Pago por Viaje: {}, la diferencia es: {}, {}'.format(productoCamion, costoCamion, ventaCamion, diferenciaCamion, balanceCamion))
