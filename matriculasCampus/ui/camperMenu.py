import os
import functions.regCamper as regCamper
import functions.manageCampers as mc
import functions.corefile as cf

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
        mc.core.checkFile(campus)
        camper = regCamper.regCamper(campus)
        #campus.update(camper)
            
        isActiveRegCamper=False


        
        