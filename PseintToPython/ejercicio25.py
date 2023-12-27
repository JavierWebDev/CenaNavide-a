# muestra la cantidad de números pares e impares

sumaP = 0
sumaI = 0

n = int(input("Ingresa el numero: "))


i=1
for i in range(1, n):
    if (i % 2) == 0:
        sumaP = sumaP + i
    else:
        sumaI = sumaI + i
print(f"SUMA IMPARES: {sumaI}")
print(f"SUMA PARES: {sumaP}")
