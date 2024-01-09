import os
import ui.mainMenu as mainm
import ui.camperMenu as camperm
import functions.manageCampers as mc
import functions.corefile as cf

campus = {
    'campus': {

    }
}

def main():
    isActiveApp = True

    while isActiveApp:
        opMainMenu = 0

        opMainMenu = mainm.mainMenu()
        
        if opMainMenu == 1:
            mc.core.checkFile(campus)
            camperm.menuRegistroCamper(campus['campus'])
            cf.AddData(campus)
            


if __name__ == "__main__":
    main()