#  busque un número que se ha generado de forma aleatoria
import random

nRandom = random.randrange(0,20)

num = int(input("Ingresa el numero a adivinar (1 - 20) : "))

if num == nRandom:
    print(f"Has acertado, el numero es: {nRandom}")
else:
    print(f"No has acertado, el numero es: {nRandom}")
