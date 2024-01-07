# Hacer un algoritmo que muestra el total a pagar por un préstamo del banco en pseint.

monto = 1000

meses = int(input("Ingresa la cantidad de meses: "))

intereses = (monto * (meses * 0.2))

total= monto + intereses

print(f"INTERESES:      {intereses}")
print(f"TOTAL A PAGAR:  {total}")