# MODULO PARA CALCULO CO2
import os

def emisionTransporte(km:float)->float:
    eTransporte = km * 0.7
    return eTransporte

def mensual(dependencia:dict):
    totalConsumo = 0.0
    try:
        potencia = int(input("[-] Ingresa la potencia del dispositivo [WATTS]:\n >) "))
        horas = int(input("[-] Ingresa las horas que se uso del disposito:\n >) "))
    except ValueError:
        os.system("cls")
        print("\033[91m[!] VALOR ERRONEO\033[0m")
        os.system("pause")
    else:
        consumoDispositivo = potencia * horas / 1000
        
        totalConsumo = consumoDispositivo + totalConsumo
        
        print(f"[*] CONSUMO DEL DISPOSITIVO = {consumoDispositivo}")
        dependencia['totalConsumo'] = totalConsumo
        dependencia['consumoDispositivos'].append(consumoDispositivo)


def periodico(periodo:int, dependencia:dict):
    try:
        consumoPeriodico = int(input(f"[-] Ingresa el consumo total en el periodo de tiempo de ({periodo} meses): "))
    except ValueError:
        os.system("cls")
        print("\033[91m[!] VALOR ERRONEO\033[0m")
        os.system("pause")
    else:
        consumoMensualPeriodico = consumoPeriodico / periodo
        
        dependencia['totalConsumo'] = consumoMensualPeriodico
        os.system("pause")
        