# tabla_informe.py


# print('{:>10s} {:>10s} {:>10s} {:>10s}'.format('Nombre', 'Cajones', 'Precio', 'Cambio'))
# print('---------- ---------- ---------- ----------')

# print('%5d %-5d %10d' % (3,4,5))


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


def hacer_informe(camiones, precios):
    lista_tuplas = []
    for camion in camiones:
        cambio = precios[camion['nombre']] - camion['precio']
        tupla = (camion['nombre'], camion['cajones'], camion['precio'], cambio)
        lista_tuplas.append(tupla)
    return lista_tuplas


camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

print('%10s %10s %10s %10s' % headers)
print('---------- ---------- ---------- ----------')

#Sin signo con tupla
#for r in informe:
    #print('%10s %10d %10s %10g' % r)

for nombre, cajones, precio, cambio in informe:
    precio_signo = '$' + str(precio)
    print(f'{nombre:>10s} {cajones:>10d} {precio_signo:>10s} {cambio:>10g}')
