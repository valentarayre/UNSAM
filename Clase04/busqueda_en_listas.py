# busqueda_en_listas.py

def buscar_u_elemento(lista, elem):
    posicion = len(lista)-1
    for item in reversed(lista):
        if item == int(elem):
            return posicion
        posicion -= 1
    return -1


def buscar_n_elemento(lista, elem):
    apariciones = 0
    for item in lista:
        if item == int(elem):
            apariciones += 1
    return apariciones


def maximo(lista):
    max = 0
    for item in lista:
        if max == 0 and item < 0:
            max = item
        elif item > max:
            max = item
    return max

