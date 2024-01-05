# Modulo que permite el registro del sismo en base a la ciudad
import os

sismos = []


def regSismos(nombre:str, ciudades:list):
    isActiveRegSismos = True
    nsis = 0

    nSismos = int(input("Ingresa el numero de sismos para cada ciudad: "))

    while isActiveRegSismos:
        for item in ciudades:

            if nombre in item:
                idx = ciudades.index(item)

                for i in range(0,nSismos):
                    sismo = float(input(f"Ingresa la categoria del sismo #{i+1}: "))
                    nsis = nsis+1

                    ciudades[idx].append(sismo)

                if nsis >= nSismos:
                    print("[!] Has alcanzado el limite de ciudades")
                    isActiveRegSismos = False
                else:
                    print("[!] No se ha encontrado la ciudad")
                    isActiveRegSismos = False
    print(ciudades)
    os.system("pause")

def categorizarSismo(categoria:int)->int:
    pass
