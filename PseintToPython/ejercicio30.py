#Ingresar una frase y mostrar la cantidad de vocales que contiene
a, e, i, o, u = 0, 0, 0, 0, 0

frase = input("INGRESA LA FRASE: ".lower())

for item in frase:
    if item == "a":
        a=+1
    elif item == "e":
        e=+1
    elif item == "i":
        i=+1
    elif item == "o":
        o=+1
    elif item == "u":
        u=+1

print("CANTIDAD DE VOCALES: ")

print(f"A -> {a}")
print(f"E -> {e}")
print(f"I -> {i}")
print(f"O -> {o}")
print(f"U -> {u}")