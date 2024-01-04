# Modulo para el registro de las ciudades
# MAX ciudades == 5
import os

ciudades = []

def regCiudad()->list:
    rta = "S"
    nCiudades = len(ciudades)+1

    if nCiudades <= 5:
        while rta in ["S","s"]:
            nombreCiudad = str(input("[*] Ingresa el nombre de la ciudad: "))

            ciudades.append([nombreCiudad])
            nCiudades = nCiudades + 1

            if nCiudades <= 5:
                rta = str(input("Deseas añadir otra ciudad? (S) SI - (N) NO: "))
            else:
                print("[!] Has alcanzado el límite de ciudades (5)")
                rta = "N"

        print(f"[*] 5 CIUDADES REGISTRADAS:\n{ciudades}")
        os.system("pause")
        
        return ciudades


