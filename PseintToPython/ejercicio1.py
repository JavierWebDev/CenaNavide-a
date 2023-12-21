# Programa que muestra la tabla de multiplicar de cualquier numero ingresado

num = int(input("Ingresa el numero de la tabla a mostrar: "))

for i in range(1,12):
    print(f"{num} x {i} = {num*i}")