# Calcula las ganancias de una Garita de Control, con cada vehículo que pasa

tarifa, van, micro, bus, man, noc = 0, 0, 0, 0, 0, 0

print("GANANCIAS DE UNA GARITA DE CONTROL")

cantidad = int(input("INGRESE CANTIDAD DE VEHICULOS: "))

for i in range(0, cantidad):
    print(f">> TIPO DE VEHICULO Nro: {i}/{cantidad}")

    print("1. Omnibus")
    print("2. Minivan")
    print("3. Micro")
    op = int(input(" > "))

    if op == 1:
        tarifa = 13
        bus=+tarifa
    elif op == 2:
        tarifa = 10
        van=+tarifa
    elif op == 3:
        tarifa = 8
        micro=+tarifa

    turno = input("INGRESE EL TURNO [M] Mañana - [N] Noche: ").upper()

    if turno == "M":
        man =+tarifa
    else:
        noc=+tarifa

print(f"IMPORTE DE TURNO MAÑANA:    {man}")
print(f"IMPORTE DE TURNO NOCHE :    {noc}")

print(f"IMPORTE DE OMNIBUS:         {bus}")
print(f"IMPORTE DE MINIVAN:         {van}")
print(f"IMPORTE DE MICRO  :         {micro}")
