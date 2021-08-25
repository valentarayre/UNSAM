# tablamult.py

def suma(num, potencia):
    count = 0
    totalSuma = 0
    while count < potencia:
        totalSuma += num
        count += 1
    return totalSuma


print('       0   1   2   3   4   5   6   7   8   9')
print('---------------------------------------------')

for num in range(10):
    cadena = ''
    for potencia in range(10):
        cadena += '%4d' % suma(num, potencia)
    print(f' {num:7>d}: {cadena}')