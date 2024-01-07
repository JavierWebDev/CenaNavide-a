# Desarrolle un algoritmo que ingrese un refrán o una frase y que indique el número de letras C, S, D, L, R y M que hay, además, que indique el número total de consonantes que tiene esa cadena de caracteres.

C, S, D, L, R, M = 0, 0, 0, 0, 0, 0 

refran = input("INGRESA REFRAN: ".upper())

for item in refran:
    if item == "C":
        C=+1
    elif item == "S":
        S=+1
    elif item == "D":
        D=+1
    elif item == "L":
        L=+1
    elif item == "R":
        R=+1
    elif item == "M":
        M=+1

print(f"TOTAL C: {C}")
print(f"TOTAL S: {S}")
print(f"TOTAL D: {D}")
print(f"TOTAL L: {L}")
print(f"TOTAL M: {M}")
print(f"TOTAL R: {R}")