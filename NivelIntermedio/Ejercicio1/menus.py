# Modulo para la gestion de menus en el programa

import os

menuBienvenida = "\n1. Registra Ciudades\n2. Registra Sismos\n3. Busca Sismos De Una Ciudad\n4. Informe De Riesgo\n5. Salir"

def menuPrincipal()->int:
    isActive = True
    header = """
    *******************************************
    *REGISTRO DE ACTIVIDAD SISMICA EN CIUDADES*
    *******************************************
    """

    while isActive:
        try:
            os.system("cls")
            print(header, menuBienvenida)
            op = int(input("\n> "))
        except ValueError:
            os.system("cls")
            print("[!] Has ingresado un valor incorrecto.")
            os.system("pause")
        else:
            return op