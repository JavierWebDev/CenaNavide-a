# Modulo para la gestion de menus en el programa

import os
import regSismos as rg

menuBienvenida = "\n1. Registra Ciudades\n2. Registra Sismos\n3. Busca Sismos De Una Ciudad\n4. Informe De Riesgo\n5. Salir"

def menuPrincipal()->int:
    isActive = True
    header = """
    *************************************************
    *   REGISTRO DE ACTIVIDAD SISMICA EN CIUDADES   *
    *************************************************
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

def menuBuscarSismos(nombre: str, ciudades: list):
    isActiveSearch = True

    header = """
    *****************************
    *   BUSCAR SISMOS X CIUDAD  *
    *****************************
    """

    while isActiveSearch:
        os.system("cls")
        print(header)

        found_city = False

        for item in ciudades:
            if nombre in item:
                found_city = True
                print(f"Los sismos de la ciudad {nombre} son:")
                for i in range(1, len(item)):
                    print(f"{i}. {item[i]}")

                isActiveSearch = False
                os.system("pause")
        
        if not found_city:
            print("La ciudad no está registrada")
            isActiveSearch = False
            os.system("pause")

def menuInformeSismico(nombre:str, ciudades:list):
    informe = True
    while informe:
        tSismos = float(0)
        header = """
        ***********************
        *   INFORME SISMICO   *
        ***********************
        """
        found_city = False

        for item in ciudades:
            if nombre in item:
                found_city = True
                for i in range(1, len(item)):

                    tSismos = tSismos + item[i]

                    informe = False
        
        if not found_city:
            print("La ciudad no está registrada")
            informe = False
            os.system("pause")

        pSismos = tSismos/(len(item))

        print(header)
        print(f"[*] EL ESTADO DE LA CIUDAD [{nombre}]:")
        print(rg.categorizarSismo(pSismos))
        os.system("pause")
        informe = False