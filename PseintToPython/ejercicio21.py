# muestre el factorial de un número ingresado

print("CALCULAR FACTORIAL")

fact = int(input("INGRESA EL NUMERO A CALCULAR: "))
total = 1

for i in range(1, fact+1):
    print(f"{(fact)-i}", end=" ")
    total = total * i

print(f"\nFACTORIAL = {total}")