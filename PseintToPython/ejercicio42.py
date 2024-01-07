# Hacer un algoritmo que muestre la unidad, la decena y la centena en pseint

num = int(input("INGRESE NUMERO DE 3 CIFRAS: "))

cen = int((num - (num % 100))/100)
res = num % 100
dec = int((res - (res % 10))/10)
uni = res % 10

print(f"CENTENA:    {cen}")
print(f"DECENA:     {dec}")
print(f"UNIDAD:     {uni}")