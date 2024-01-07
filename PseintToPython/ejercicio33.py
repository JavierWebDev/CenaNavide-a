# Hacer algoritmo que calcule el salario a pagar de un empleado, con un descuento del 20%

salario = int(input("Ingrese salario: "))

desc = salario * 0.20

print(f"EL DESCUENTO ES: {desc}")
print(f"EL TOTAL A PAGAR ES: {salario-desc}")