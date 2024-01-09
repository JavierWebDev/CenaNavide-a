import os

opcionesMainMenu = ["Registro De Campers","Registrar Prueba De Seleccion","Crear Ruta De Aprendizaje","Registrar Trainer","Gestior De Matriculas","Ingresar Notas Camper (Campers Inscritos)","Reportes"]

def mainMenu():
    header = '''
    ┌───────────────────────────┐
    │                           │
    │   SEGUIMIENTO ACADEMICO   │
    │                           │
    └───────────────────────────┘
    '''
    os.system("cls")
    print(header)
    for i,item in enumerate(opcionesMainMenu):
        print(f"{i+1}. {item}")

    try:
        op = int(input(" >) "))
    except ValueError:
        print("\033[91m[!] VALOR ERRONEO\033[0m")
        os.system("pause")
    else:
        return op