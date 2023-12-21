# muestre la serie : 1 + 2/3 + 3/5 + 4/7

num = int(input("VALOR DE N: "))
suma = 1
d = 3
i=2

if num > 1:
    print(f"{suma} +",end=" ")
    for i in range(1,num):
        if (i == num):
            print(f"{i}/{d}",end=" ")
        else:
            print(f"{i}/{d} +",end=" ")
        suma = suma + (i/d)
        d = d+2
print("")
print(f"SUMA = {suma}")