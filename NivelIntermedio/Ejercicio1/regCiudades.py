# Modulo para el registro de las ciudades
# MAX ciudades == 5
import os

def regCiudad(ciudades:list):
    rta = "S"
    nCiudades = len(ciudades)

    if nCiudades <= 5:
        while rta in ["S","s"]:
            nombreCiudad = str(input("[*] Ingresa el nombre de la ciudad: "))

            ciudades.append([nombreCiudad])
            nCiudades = nCiudades + 1

            rta = str(input("Deseas añadir otra ciudad? (S) SI - (N) NO: "))
            if rta in ['N','n']:
                print("¨[*] Volviendo al menu principal")
                rta = 'n'

    else:
        print("[!] Has alcanzado el límite de ciudades (5)")
        rta = "N"

        print(f"[*] {nCiudades} CIUDADES REGISTRADAS:\n{[ciudades]}")
        os.system("pause")



