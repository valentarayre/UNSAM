# propaga.py

def propagar(lista):
    propagado = []
    pos = 0
    for e in lista:
        if not (len(propagado) > pos):
            if e == 0 or e == -1:
                propagado.append(e)
            elif e == 1:
                for i in reversed(range(pos)):
                    if lista[i] == -1:
                        break
                    propagado[i] = 1
                for i in range(len(lista)):
                    if (pos-1) < i:
                        if lista[i] == -1:
                            break
                        propagado.append(1)
        pos += 1
    return propagado


print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
