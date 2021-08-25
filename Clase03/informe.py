# informe.py
import csv


def leer_camion(ruta):
    with open(ruta, 'r', encoding='UTF-8') as file:
        rows = csv.reader(file)
        encabezados = next(rows)
        lista = []
        for n_fila, fila in enumerate(rows, start=1):
            record = dict(zip(encabezados, fila))
            camion = {}
            try:
                camion['nombre'] = record['nombre']
                camion['cajones'] = int(record['cajones'])
                camion['precio'] = float(record['precio'])
                lista.append(camion)
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        return lista


def leer_precios(ruta):
    with open(ruta, 'r', encoding='UTF-8') as file:
        rows = csv.reader(file)
        lista = {}
        for row in rows:
            if row:
                lista[row[0]] = float(row[1])

        return lista


camiones = leer_camion('../Data/fecha_camion.csv')
precios = leer_precios('../Data/precios.csv')

for camion in camiones:
    costoCamion = round(camion['cajones'] * camion['precio'], 2)
    if camion['nombre'] in precios:
        ventaCamion = round(precios[camion['nombre']] * camion['cajones'], 2)
        diferenciaCamion = round(ventaCamion - costoCamion, 2)

        if diferenciaCamion > 0:
            balanceCamion = 'Hubo Ganancia'
        else:
            balanceCamion = 'Hubo Perdida'

        print(
            f'Producto: {camion["nombre"]},'
            f'Costo del Camion: {costoCamion}, '
            f'Pago por Viaje: {ventaCamion}, '
            f'la diferencia es: {diferenciaCamion}, {balanceCamion}'
            )
    else:
        print('falta Producto')
