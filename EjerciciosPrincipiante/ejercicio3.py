'''
Teniendo en cuenta el punto 2 se requiere tener el registro de 20 estudiantes y poder determinar
el estado de salud de la comunidad estudiantil. El programa debe mostrar el siguiente reporte:

a. Cuantos estudiantes se encuentran en el peso ideal.
b. Cuantos estudiantes se encuentran en obesidad grado I
c. Cuantos estudiantes se encuentran en obesidad grado II
d. Cuantos estudiantes se encuentran en obesidad grado III
e. Cuantos estudiantes se encuentran en Sobrepeso

'''
import os

isActive = True
estudiantesMax = 20

nPesoIdeal = 0
nSobrepeso = 0
nObesidadI = 0
nObesidadII = 0
nObesidadIII = 0
desnutricion = 0

def calcularIMC(peso:float, altura:float)->float:
    imc = peso/(altura*altura)
    return imc


try:
    for i in range(0,estudiantesMax):
        os.system("clear")

        nombre = str(input("Ingresa el nombre del estudiante: "))
        edad = int(input("Ingresa la edad del estudiante: "))
        peso = float(input("Ingresa el peso del estudiante: "))
        altura = float(input("Ingresa la altura del estudiante: "))

        if (calcularIMC(peso, altura) >= 18.5 and calcularIMC(peso, altura) < 25):
            categoría = "Normal"
            nPesoIdeal=+1
        elif (calcularIMC(peso, altura) >= 25 and calcularIMC(peso, altura) < 30):
            categoría = "Sobrepeso"
            nSobrepeso=+1
        elif (calcularIMC(peso, altura) >= 30 and calcularIMC(peso, altura) < 35):
            categoría = "Obesidad I"
            nObesidadI=+1
        elif (calcularIMC(peso, altura) >= 35 and calcularIMC(peso, altura) < 40):
            categoría = "Obesidad II"
            nObesidadII=+1
        elif (calcularIMC(peso, altura) >= 40):
            categoría = "Obesidad III"
            nObesidadIII=+1
        else:
            desnutricion=+1
            
        op = input("Desea agregar otro usuario [S](si) - [N](no)").upper()

        if (op == "S"):
            isActive = True
            os.system("pause")
            os.system("clear")

        elif (op == "N") or (i == estudiantesMax):
            isActive = False
            print("Saliendo del programa...")
            os.system("pause")
            

except ValueError:
    print("Error al ingresar los datos!")
    os.system("pause")
        
os.system("clear")

print(f"DESNUTRICION:                   {desnutricion}")
print(f"TOTAL PESO IDEAL:               {nPesoIdeal}")
print(f"TOTAL SOBREPESO:                {nSobrepeso}")
print(f"TOTAL OBESIDAD I:               {nObesidadI}")
print(f"TOTAL OBESIDAD II:              {nObesidadII}")
print(f"TOTAL OBESIDAD III:             {nObesidadIII}")