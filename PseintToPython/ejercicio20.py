# muestra el promedio de varias notas ingresadas

print("PROMEDIO DE NOTAS")
nNotas = int(input("Ingrese en numero de notas: "))

suma = 0

for i in range(nNotas):
    nota = int(input(f"NOTA {i+1}: "))
    suma = suma + nota

print(f"El promedio de las notas es: {suma/nNotas}")