# Hacer un algoritmo que al ingresar las horas, minutos y segundos, calcule el costo total

H = int(input("HORAS: "))
M = int(input("MINUTOS: "))
S = int(input("SEGUNDOS: "))

costo = ((H * 3600) + (M * 60) + S) * 0.25

print(f"EL COSTO TOTAL ES:  {costo}")