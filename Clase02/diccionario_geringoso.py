# diccionario_geringoso.py

def geringoso(palabra):
    capadepenapa = ''
    for c in palabra:
        capadepenapa += c
        if c.lower() in 'aeiou':
            capadepenapa += 'p' + c.lower()
    return capadepenapa


def diccionarioGeringoso(lista):
    diccionario = {}
    for item in lista:
        diccionario[item] = geringoso(item)
    return diccionario


lista = ['banana', 'manzana', 'mandarina']
print(diccionarioGeringoso(lista))
