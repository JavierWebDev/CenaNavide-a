"""
2. La alcaldía de Bucaramanga desea realizar un programa que le permita calcular el valor de CO2 producido
En las diferentes instalaciones gubernamentales de la ciudad. Tenga en cuenta las siguientes observaciones:

    
Consumo de electricidad:
    - Obtener facturas de electricidad y verificar consumo mensual o anual
    - Utiliza el factor de emision para para convertir el consumo electrico a emisiones de CO2
    
    EMISION CO2 = Consumo electrico X Factor de emision
    
FACTURA:
    - kWh (kilovatios por hora en el periodo facturado)
    - Periodo facturado

CALCULO DEL CONSUMO MENSUAL O ANUAL:
    - Si se muestra el consumo mensual no se necesita realizar mas calculos
    - Consumo bimestral, trimestral, etc... -> CONSUMOMENSUAL / # MESESPERIODO

CONSUMO X DISPOSITIVO:
    - CONSUMODISPOSITIVO = POTENCIADELDISPOSITIVOW x HORASDEUSO / 1000
    - TOTAL = SUMA CONSUMO DISPOSITIVOS

EMISION X TRANSPORTE:
    - KM RECORRIDOS X FACTOR EMISION TRANSPORTE

El programa debe permitir mostrar cual de las instalaciones tiene mayor producción de CO2.
Requerimientos: El programa debe contar con un menú principal que permita realizar todos los
Procesos solicitados.

1. Registrar Dependencia
2. Registrar consumo por dependencia : Tengan en cuenta que se debe registrar los valores
consumidos por los dispositivos en cada una de las oficinas.
3. Ver CO2 producido
4. Dependencia que produce mayor CO2
5. Salir
"""
# PROGRAMA PRINCIPAL
import os
import menus as menu
import dependencias as dp

isAppActive = True

dependencias = {}

while isAppActive:
    try:
        opMenuPrincipal = menu.menuPrincipal()
    except ValueError:
        print("\033[91m[!] ERROR EN LA OPCION\033[0m")
        os.system("pause")
    else:
        
        if opMenuPrincipal == 1:
            rta = "S"
            while rta == "S":
                dependencias.update(dp.regDependencia())
                rta = str(input("[?] Desea Registrar Otra Depedencia [S] Si - [N] No\n    >) ").upper())

        elif opMenuPrincipal == 2:
            menu.menuRegistrarCosumo(dependencias)
            
        elif opMenuPrincipal == 3:
            menu.verCO2(dependencias)
        elif opMenuPrincipal == 4:
            os.system("cls")
            print(f"EL MAYOR CO2: {menu.mayorCO2(dependencias)}")
            os.system("pause")
        elif opMenuPrincipal == 5:
            print("[!] SALIENDO")
            os.system("pause")