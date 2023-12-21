# Hacer un algoritmo que calcule el monto a pagar por 10 compras realizadas

total = 0
producto = 0

for i in range(0,10):
    producto = int(input(f"Ingresa el valor del producto {i+1}: "))
    total = total + producto
if total > 50:
    desc = total * 0.7
    print(f"Total (DESCUENTO): {total - desc}")
else: 
    print(f"Total: {total}")