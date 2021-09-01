# invlista.py

def invertir_lista(lista):
    invertida = []
    longitud = len(lista) -1
    for e in range(len(lista)):
        invertida.append(lista[longitud])
        longitud -= 1
    return invertida

print(invertir_lista([1, 2, 3, 4, 5]))