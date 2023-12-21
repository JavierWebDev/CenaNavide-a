# muestre el producto de varios números ingresados

pro = 1

n = int(input("Ingrese el numero: "))

for i in range(0, n):
    print(f"{i+1} ", end="")
    pro = pro * (i+1)
print(f"\nEl producto de los numeros es: {pro}")