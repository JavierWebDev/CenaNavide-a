# MODULO PARA EL REGISTRO Y MANEJO DE LAS DEPENDENCIAS
import os
import emisionCO2 as ec


def regDependencia()->dict:
    global dependencia
    header = '''
    *****************************
    *   REGISTRAR DEPENDENCIA   *
    *****************************
    '''
    
    
    os.system("cls")
    print(header)
        
    nombre = input("[-] Ingresa el nombre de la dependencia: ")
        
    dependencia = {
    'nombre': nombre,
    'consumoDispositivos':[],
    'totalConsumo':0.0,
    'emisionTransporte':0.0
    }
        
    return {nombre : dependencia}
        
def regConsumo():
    header = '''
    ***************************
    *   REGISTRO DE CONSUMO   *
    ***************************
    '''
    
    isActiveConsuption = True
    while isActiveConsuption:
        try:
            os.system("cls")
            print(header)
            print("Registrar Consumo:\n\n1. Emision Por Transporte\n2. Registrar Emision Por Dispositivos\n3. Salir")    
            op = int(input("\n >) "))
        
        except ValueError:
            print("\033[91m[!] ERROR EN LA OPCION\033[0m")
            os.system("pause")
            
        else:
            if op == 1:
                try:
                    os.system("cls")
                    print(header)
                    km = float(input("[-] Ingresa los kilometros recorridos: "))
                except ValueError:
                    print("\033[91m[!] ERROR EN LA OPCION\033[0m")
                else:
                    os.system("cls")
                    dependencia['emisionTransporte'] = ec.emisionTransporte(km)
                    print(f"[*] FACTOR DE EMISION: {dependencia['emisionTransporte']}   |   \033[92m[ REGISTRADO CORRECTAMENTE ]\033[0m")
                    os.system("pause")
                    
            
            elif op == 2:
                try:
                    os.system("cls")
                    print(header)
                    periodoTiempo = int(input("[-] Ingresa el periodo de tiempo en el que esta el consumo [1 -> Mensual, 2 -> Bimensual, etc...]: "))
                except ValueError:
                    os.system("cls")
                    print("\033[91m[!] VALOR ERRONEO\033[0m")
                    os.system("pause")
                else:
                    if periodoTiempo == 1:
                        rta = "S"
                        while rta == "S":
                            ec.mensual(dependencia)
                            rta = str(input("[?] Desea Registrar Otro Dispositivo? [S] Si - [N] No\n    >) ").upper())
                        isActiveConsuption = False
                    elif periodoTiempo > 1:
                        ec.periodico(periodoTiempo, dependencia)
                        isActiveConsuption = False
                    else:
                        print("\033[91m[!] VALOR ERRONEO\033[0m")
                        
            
            elif op == 3:
                os.system("cls")
                print("\033[91m[!] VOLVIENDO AL MENU DE REGISTRO DE CONSUMO\033[0m")
                isActiveConsuption = False
                os.system("pause")
            
    