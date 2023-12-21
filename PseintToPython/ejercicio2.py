par = 0 
impar = 0

for i in range(0,10):
    num = int(input("Ingresa el numero (1 - 10): "))
    if (num % 2) == 0:
        par= par + 1
    else:
        impar= impar + 1

print(f"La cantidad de numeros impares es: {impar}")
print(f"La cantidad de numeros pares es: {par}")
