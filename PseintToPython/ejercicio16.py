# muestra si un número es o no capicúa

num = str(input("Ingrese el numero: "))

rev = num[::-1]

print(f"NUMERO: {num}")
print(f"NUMERO REVERSO: {rev}")

if rev == num:
    print(f"El numero: {num} | CAPICUA")
else:
    print(f"El numero: {num} | NO CAPICUA")