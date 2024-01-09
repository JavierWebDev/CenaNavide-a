import os
import functions.manageCampers as mc
import functions.corefile as core

campers= {}

def regCamper()->dict:
    isActive = True
    while isActive:
        try:
            os.system("cls")
            id = int(input("[-] Ingresa el ID del camper: "))
            nombre = input("[-] Ingresa el nombre del camper: ")
            apellido = input("[-] Ingresa el apellido del camper: ")
        except ValueError:
            print("\033[91m[!] VALOR ERRONEO\033[0m")
            os.system("pause")
        else:
            camper = {
                'ID':id,
                'nombre':nombre,
                'apellido':apellido,
                'acudiente':{},
                'telefonos':{}

            }
            
            acudiente = {
                'ID':'00',
                'nombre':'xx',
                'telefono':'00',
                'email':'xx'
            }
            telefonos = {
                'telefonos':[]
            }
            telefono = {
                'ubicacion':'xx',
                'numero': '00'
            }
            isActiveRegAcudiente = True

            while isActiveRegAcudiente:

                os.system("cls")
                acudienteTitulo = '''
                ┌─────────────────────────┐
                │                         │
                │   REGISTRAR ACUDIENTE   │
                │                         │
                └─────────────────────────┘
                '''
                print(acudienteTitulo)

                try:
                    acudiente['ID'] = int(input("[-] Ingresa ID del acudiente: "))
                    acudiente['nombre'] = input("[-] Ingresa nombre del acudiente: ")
                    acudiente['telefono'] = input("[-] Ingresa telefono del acudiente: ")
                    acudiente['email'] = input("[-] Ingresa email del acudiente: ")
                except ValueError:
                    print("\033[91m[!] VALOR ERRONEO\033[0m")
                    os.system("pause")
                else:
                    camper['acudiente'].update(acudiente)
                    print(camper)
                    print("\n\033[92m[ ACUDIENTE REGISTRADO CORRECTAMENTE ]\033[0m")
                    isActiveRegAcudiente = False
                    os.system("pause")
                               
            telefonoTitulo = '''
            ┌─────────────────────────┐
            │                         │
            │   REGISTRAR TELEFONO    │
            │                         │
            └─────────────────────────┘
            '''


            rta = "S"
            while rta == "S":
                os.system("cls")
                print(telefonoTitulo)
                telefono['ubicacion'] = input("[-] Ingresa ubicacion (Casa, Trabajo, etc..): ")
                telefono['numero'] = input("[-] Ingresa Nro telefonico: ")

                telefonos['telefonos'].append(telefono)
                rta = input("[?] Deseas Ingresar otro numero telefonico? (S [SI] - (N [NO]): ").upper()
                if rta == "S":
                    rta = "S"
                else:
                    rta = "N"
                    isActive = False
            print("\n\033[92m[ ACUDIENTE REGISTRADO CORRECTAMENTE ]\033[0m")

            isActive = False
            camper.update(telefonos)
            return {camper['ID']:camper}