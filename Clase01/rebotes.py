# rebotes.py

#Valor Inicial (Altura Inicial del rebote)
rebotes = 100

#Logica un for que va 1 a 10, mostrando el rebote
#Sin round
#for i in range(1, 11):
#    rebotes = (rebotes * 3) / 5
#    print(i, rebotes)

#Con round
for i in range(1, 11):
    rebotes = (rebotes * 3) / 5
    print(i, round(rebotes,5))
