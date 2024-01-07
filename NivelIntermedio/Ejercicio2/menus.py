# MODULO MANEJO DE MENUS
import os
import dependencias as dp

opcionesMenuPrincipal = "\n1. Registrar Dependencias\n2. Registrar Consumo por dependencia\n3. Ver CO2 Producido Por Dependencia\n4. Dependencia Con Mayor CO2\n5. Salir"

def menuPrincipal()->int:
    os.system("cls")
    header = """
    *********************
    *   CO2 PRODUCIDO   *
    *********************
    """
    isActiveMenuPrincipal = True
    
    while isActiveMenuPrincipal:
        os.system("cls")
        
        print(header, opcionesMenuPrincipal)
        
        try:
            op = int(input("\n >) "))
        except ValueError:
            print("\033[91m[!] ERROR EN LA OPCION\033[0m")
            os.system("pause")
        else:
            return op

def menuRegistrarCosumo(dependencias:dict):
    header = '''
    ************************
    *   REGISTRO CONSUMO   *
    ************************
    '''
    isActiveRegConsumo = True
    while isActiveRegConsumo:
        try:
            os.system("cls")
            print(header)
            bDependencia = str(input("[*] Ingresa la dependencia para registrar su consumo: "))
        except ValueError:
            print("\033[91m[!] ERROR EN LA OPCION\033[0m")
            os.system("pause")
        else:
            found = False
            
            for item in dependencias:
                if bDependencia in item:
                    found = True
                    os.system("cls")
                    dp.regConsumo()
                    isActiveRegConsumo = False
                    break
                
            if not found:
                os.system("cls")
                print("\033[91m[!] NO SE HA ENCONTRADO LA DEPENDENCIA\033[0m")
                os.system("pause")
                isActiveRegConsumo = False
                
def verCO2(dependencias:dict):
    header = '''
    ************************
    *   VER CO2 GENERADO   *
    ************************
    '''
    try:
        os.system("cls")
        print(header)
        bDependencia = str(input("[*] Ingresa la dependencia para ver el CO2 generado: "))
    except ValueError:
            print("\033[91m[!] ERROR EN LA OPCION\033[0m")
            os.system("pause")
    else:
        found = False
            
        for item in dependencias:
            if bDependencia in item:
                found = True
                os.system("cls")
                # CODIGO
                factorEmisionDispositivos = dependencias[bDependencia]["totalConsumo"] * 0.2
                
                
                print(f"\033[93m[ CO2 GENERADO POR DISPOSITIVOS ]: {factorEmisionDispositivos}\033[0m")
                print(f"\033[93m[ CO2 GENERADO POR TRAN ]: {dependencias[bDependencia]["emisionTransporte"]}\033[0m")
                
                os.system("pause")
                break
        if not found:
            os.system("cls")
            print("\033[91m[!] NO SE HA ENCONTRADO LA DEPENDENCIA\033[0m")
            os.system("pause")
        
def mayorCO2(dependencias:dict)->str:
    buscar = 'totalConsumo'
    
    valores = max(dependencias[buscar] for dependencias in dependencias.values() if buscar in dependencias)
    
    return valores
