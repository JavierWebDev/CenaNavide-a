# muestre la serie gráfica de números 123456789 en forma decreciente

i=1
j=1

for i in range(0,9):
    serie = 0
    for j in range(10-i):
        serie = (serie * 10) + j
    print(serie)