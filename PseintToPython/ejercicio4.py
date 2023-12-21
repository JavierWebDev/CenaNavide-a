# Hacer un algoritmo que muestre el nombre y el promedio del alumno

xpro = 0

for i in range(0, 5):
    nom = str(input("Ingresa el nombre del estudiante: "))
    pro = int(input("Ingresa el promedio del estudiante: "))
    
    if pro > xpro:
        xpro = pro
        xnom = nom
    
print(f"El estudiante con la mayor nota es: {xnom}")    
print(f"La mayor nota es: {xpro}")