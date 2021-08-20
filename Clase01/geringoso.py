# geringoso.py

cadena = 'Geringoso'
capadepenapa = ''
for c in cadena:
    if c.lower() == 'a':
        capadepenapa += c + 'pa'
    elif c.lower() == 'e':
        capadepenapa += c + 'pe'
    elif c.lower() == 'i':
        capadepenapa += c + 'pi'
    elif c.lower() == 'o':
        capadepenapa += c + 'po'
    elif c.lower() == 'u':
        capadepenapa += c + 'pu'
    else:
        capadepenapa += c

print(capadepenapa)