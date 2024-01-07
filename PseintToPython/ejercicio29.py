# Hacer un programa dónde se tienen 10 niños a quienes se les pide sus datos personales como DNI, Fecha de nacimiento (considerar día, mes y año) y género. Si los niños tienen 8 años o más se les dará Tablet. Si los niños tienen 6 años se les dará carrito o muñeca dependiendo del género.

diax = 7
mesx = 1
aniox = 2024

for i in range(0,10):
    dni = input("DNI: ")
    dian = int(input("DIA NACIMIENTO: "))
    mesn = int(input("MES DE NACIMIENTO: "))
    anion = int(input("AÑO DE NACIMIENTO: "))
    genero = str(input("INGRESA SEXO ([H] - Hombres | [M] - Mujeres): ").upper())

    print(f"FECHA ACTUAL: {diax} / {mesx} / {aniox}")

    edad = aniox - anion

    if mesn > mesx:
        edad = edad -1
    else:
        if mesn == mesx and diax < dian:
            edad = edad - 1
    print(f"EDAD: {edad}")

    if edad >= 9:
        print("RECIBE TABLET")
    elif edad < 9:
        if genero == "H":
            print("RECIBE CARRO")
        elif genero == "M":
            print("RECIBE MUÑECA")
