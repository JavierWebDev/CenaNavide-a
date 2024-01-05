# Modulo que permite el registro del sismo en base a la ciudad
import os

sismos = []


def regSismos(ciudades:list):
    nsis = 0
    isActiveRegSismos = True
    nSismos = int(input("Ingresa el numero de sismos para cada ciudad: "))
    header="""
    ************************
    *   REGISTRAR SISMOS   *
    ************************
    """

    while isActiveRegSismos:
        print(header)
        for item in ciudades:

            idx = ciudades.index(item)

            for i in range(0,nSismos):
                sismo = float(input(f"Ingresa la categoria del sismo #{i+1} para la ciudad [{item[0]}]: "))
                nsis = nsis+1

                ciudades[idx].append(sismo)

            if nsis >= nSismos:
                print("[!] Has alcanzado el limite de sismos")
                isActiveRegSismos = False
    os.system("pause")

def categorizarSismo(pSismos:float)->str:
    categoria = ""

    if pSismos > 2.5:
        categoria = "\033[93m[ AMARILLO ] - SIN RIESGO\033[0m"
    elif pSismos >= 2.5 and pSismos < 4.5:
        categoria = "\033[33;91m[ NARNAJA ] - RIESGO MEDIO\033[0m"
    elif pSismos >= 4.5:
        categoria = "\033[91m[ ROJO ] - RIESGO ALTO\033[0m"

    return categoria

