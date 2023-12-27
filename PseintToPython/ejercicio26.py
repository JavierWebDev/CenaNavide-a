# Muestra el total de ventas realizadas y calcula el porcentaje de cuantas fueron por mujeres

nEmpleados = 0
nMujeres = 0
vHombres = 0
vMujeres = 0
tVentas = 0

print("TOTAL DE VENTAS POR SEXO")
nEmpleados = int(input("CANTIDAD DE EMPLEADOS: "))

for i in range(0, nEmpleados):
    nombre = str(input("INGRESA NOMBRE: "))
    sexo = str(input("INGRESA SEXO (H o M): ").upper())
    ventas = int(input("INGRESA VENTAS DEL EMPLEADO: "))

    if sexo == "H":
        vHombres = vHombres + ventas
    else: 
        vMujeres = vMujeres + ventas
        nMujeres = nMujeres + 1

print(f"VENTAS MUJERES: {vMujeres}")
print(f"VENTAS HOMBRES: {vHombres}")
print(f"% VENTAS MUJERES: {(nMujeres *100) / nEmpleados}%")