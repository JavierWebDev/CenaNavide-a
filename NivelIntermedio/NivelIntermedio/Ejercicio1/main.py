'''
1. El centro de prevención de sismos en Colombia desea realizar un programa que le permita llevar el
Registro del los sismos presentados en 5 ciudades del país. Por cada ciudad se realizan n cantidad de
Registros. El programa debe permitir registrar las muestras del movimiento en cada ciudad.
Requerimientos:
1. El programa debe tener un menú con las siguientes opciones
1. Registrar Ciudad
2. Registrar Sismo
3. Buscar sismos por ciudad
4. Informe de riesgo
5. Salir

Restricciones:
1. Todas las ciudades deben tener la misma cantidad de sismos registrado
2. El informe de riesgos presenta la siguiente clasificación:
1. Amarillo (Sin riesgo) : El promedio de los sismos es < 2,5
2. Naranja (Riesgo medio) : El promedio de los sismos esta entre 2.6 y 4.5
3. Rojo (Riesgo alto) : El promedio de los sismos es mayor a 4.5
La solución debe implementar listas , listas dentro de listas y modulos
'''
import os
import menus as menu
import regCiudades as rc
import regSismos as rs

# Lista en la que se almacenaran los datos
informeSismico = []

isActive = True
while isActive:
    try:
        opMenu = menu.menuPrincipal()
    except ValueError:
        print("[!] La opcion es incorrecta")
        os.system("pause")
    else:
        if opMenu == 1:
            os.system("cls")
            rc.regCiudad(informeSismico)

        elif opMenu == 2:
            os.system("cls")
            nombreCiudad = str(input("Ingresa el nombre de la ciudad a la cual registrar sismos: "))
            rs.regSismos(nombreCiudad, informeSismico)

        elif opMenu == 3:
            pass
            os.system("pause")
        
        elif opMenu == 4:
            pass
            os.system("pause")
        
        elif opMenu == 5:
            os.system("pause")
            print("[!] Has seleccionado salir del programa")
            break

