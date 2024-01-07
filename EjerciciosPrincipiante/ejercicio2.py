'''
El centro de salud de campuslands desea realizar un programa que le permita calcular el IMC de los Estudiantes nuevos.

El programa debe mostrar el nombre del estudiante, la edad, el imc y la categoría según el IMC obtenido

CATEGORIAS:

Normal -> 18.5 - 24.9
Sobrepeso -> 25 - 29.9
Obesidad I -> 30 - 34,9
Obesidad II -> 35 - 39,9
Obesidad III -> 40 <

'''

import os

isActive = True

def calcularIMC(peso:float, altura:float)->float:
    imc = peso/(altura*altura)
    return imc

while isActive:
    try:
        nombre = str(input("Ingresa el nombre del estudiante: "))
        edad = int(input("Ingresa la edad del estudiante: "))
        peso = float(input("Ingresa el peso del estudiante: "))
        altura = float(input("Ingresa la altura del estudiante: "))

        if (calcularIMC(peso, altura) >= 18.5 and calcularIMC(peso, altura) < 25):
            categoría = "Normal"
        elif (calcularIMC(peso, altura) >= 25 and calcularIMC(peso, altura) < 30):
            categoría = "Sobrepeso"
        elif (calcularIMC(peso, altura) >= 30 and calcularIMC(peso, altura) < 35):
            categoría = "Obesidad I"
        elif (calcularIMC(peso, altura) >= 35 and calcularIMC(peso, altura) < 40):
            categoría = "Obesidad II"
        elif (calcularIMC(peso, altura) >= 40):
            categoría = "Obesidad III"

        os.system("clear")

        print(f"NOMBRE:                 {nombre}")
        print(f"EDAD:                   {edad}")
        print(f"IMC:                    {calcularIMC(peso, altura)}")
        print(f"CATEGORIA:              {categoría}")

    except ValueError:
        print("Error al ingresar los datos!")
        os.system("pause")