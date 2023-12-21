# muestre todos los números que estén en el rango de A y B

num1 = int(input("NUMERO 1: "))
num2 = int(input("NUMERO 2: "))

if num1 < num2:
    for i in range(num1-1, num2):
        print(i, end=" ")
else:
    print("El rango no existe")