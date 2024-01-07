# Leer 3 numeros enteros positivos e imprima la sumatoria de los 3 numeros
import os

isActive = True

while isActive:
    try:
        os.system("clear")
        a = int(input(">"))
        b = int(input(">"))
        c = int(input(">"))

        if (a >= 0) and (b >= 0) and (c >= 0):
            print(f"La suma de {a}, {b} y {c} = {a+b+c}")

        op = bool(input("Desea hacer otra operacion? [S](si) - [Enter](no)"))
        if (op == True):
            isActive = True
            os.system("pause")
            os.system("clear")

        else:
            isActive = False
            print("Saliendo del programa...")
            os.system("pause")

    except ValueError:
        print("Ingresa un valor entero")
        os.system("pause")