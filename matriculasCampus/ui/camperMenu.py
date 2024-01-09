import os
import functions.regCamper as regCamper
import functions.manageCampers as manage

def menuRegistroCamper(campus:dict):
    header = '''
    ┌──────────────────────┐
    │                      │
    │   REGISTRAR CAMPER   │
    │                      │
    └──────────────────────┘
    '''

    os.system("cls")
    isActiveRegCamper = True
    while isActiveRegCamper:
        print(header)
        campus.update(regCamper.regCamper())
        
            
        isActiveRegCamper=False
        os.system("pause")


        
        