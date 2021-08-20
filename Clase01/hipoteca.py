# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

mes = 0

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    mes += 1

    if (mes >= pago_extra_mes_comienzo) and (mes <= pago_extra_mes_fin):

        saldo = saldo * (1 + tasa / 12) - pago_mensual - pago_extra
    else:
        saldo = saldo * (1 + tasa / 12) - pago_mensual
    #Si el numero es negativo mayor a 0 significa que pago lo que debia y sobro dinero
    if saldo < 0:
        saldo = 0

    total_pagado = total_pagado + pago_mensual
    print(mes, total_pagado, round(saldo,2))

print('Total pagado', round(total_pagado, 2))
print('Meses', mes)