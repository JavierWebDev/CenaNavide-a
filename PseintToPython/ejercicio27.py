# Hacer un programa dónde en una Corporación comercial se registra el nombre, género y la cantidad de ventas realizado durante el mes de cada uno de sus N empleados, se pide calcular el total de ventas realizadas por género durante el mes así con el porcentaje de mujeres que trabajan en la corporación.

nEmpleados = int(input("Ingresa el numero de empleados a registrar: "))

nh = 0
nm = 0
nVH = 0
nVM = 0

for i in range(0, nEmpleados):
    print(f"EMPLEADO #{i+1}: ")
    nombre = str(input("INGRESA NOMBRE: "))
    genero = str(input("INGRESA SEXO ([H] - Hombres | [M] - Mujeres): ").upper())
    venta = int(input("INGRESA VENTAS: "))

    if genero == "H":
        nh = nh + 1
        nVH = nVH + venta
    elif genero == "M":
        nm = nm + 1
        nVM = nVM + venta
    else: 
        print("Error ingresando el genero")

totalEmpleados = nh + nm

print(f"VENTAS DE HOMBRES: {nVH}")
print(f"VENTAS DE MUJERES: {nVM}")
print(f"PORCENTAJE DE MUJERES: {(nm*100)/totalEmpleados}%")