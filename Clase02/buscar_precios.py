# buscar_precios.py

def buscar_precio(buscar):
    archivo = '../Data/precios.csv'
    lista = {}
    with open(archivo, 'rt', encoding='UTF-8') as file:
        data = file.read()
        lineas = data.split()
        for linea in lineas:
            producto = linea.split(',')
            lista[producto[0]] = producto[1]
        if buscar in lista:
            print('El precio de un cajon de', buscar, 'es:', lista[buscar])
        else:
            print(buscar, 'no figura en el listado de precios.')


buscar_precio('Frambuesa')
buscar_precio('Kale')
