# Mostrar serie fibonacci

A = 0
B = 1
C = 0

for i in range(0, 10):
    print(f"{C}\n")
    A = B
    B = C
    C = A + B
