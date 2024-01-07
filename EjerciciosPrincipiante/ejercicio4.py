'''
4. Se desea realizar un programa en Python que permita ingresar n números enteros positivos y cuando se
Ingrese un numero negativo debe mostrar en pantalla el siguiente reporte.

a. Total de números ingresados
b. Total de números pares ingresados
c. Promedio de los números pares
d. Promedio de los números impares
e. Cuantos números son menores que 10
f. Cuantos números están entre 20 y 50
g. Cuantos números son mayores que 100
'''

tNumeros = 0
tNumerosPares = 0
tNumerosImpares = 0
pPares = 0
pImpares = 0
nMenores10 = 0
nEntre20y50 = 0
nMayores50 = 0

n = int(input("INGRESA # ENTEROS POSITIVOS A REGISTRAR: "))

isActive = True

while isActive:
    num = int(input("Ingresa un numero entero positivo para registrar: "))
    if num >= 0:
        tNumeros = tNumeros + 1
        
        for i in range(0, n):
            if (num % 2) == 0:
                tNumerosPares = tNumerosPares+1
            elif (num % 2) > 0:
                tNumerosImpares = tNumerosImpares+1


    else:
        isActive = False