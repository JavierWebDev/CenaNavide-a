# muestra si un número ingresado es primo

num = int(input("Ingresa el numero: "))

es_primo = True

for i in range(2, num + 1):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            es_primo = False
            break
if (es_primo == True):
    print("NUMERO PRIMO")
else:
    print("NO ES NUMERO PRIMO")