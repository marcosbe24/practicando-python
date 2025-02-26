numeros = [5,12,34,7,19,25,8,3,16,22,100]

for nume in numeros:
    if nume <= 16:
        print(f"se omite este valor {nume}")
        continue
    else:
        print(nume)