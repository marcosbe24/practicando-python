while True:
    valor = input("ingrese lo que quiere hacer (sumar,restar,multiplicar,dividir) :").strip().lower()

    if valor == "salir":
        break

    elif valor in ["sumar","suma"]:
        valor_1 = int(input("ingrese el numero 1:"))
        valor_2 = int(input("ingrese el numero 2:"))
        valor_3 = valor_1 + valor_2
        print("la suma es:",valor_3)

    elif valor in ["restar","resta",]:
        valor_1 = int(input("ingrese el numero 1:"))
        valor_2 = int(input("ingrese el numero 2:"))
        valor_3 = valor_1 - valor_2
        print("la resta es:",valor_3)

    elif valor in ["multiplicar","multiplicacion","mult"]:
        valor_1 = int(input("ingrese el numero 1:"))
        valor_2 = int(input("ingrese el numero 2:"))
        valor_3 = valor_1 * valor_2
        print("la multiplicacion es:",valor_3)

    elif valor in ["dividir","division","div"]:
        valor_1 = int(input("ingrese el numero 1:"))
        valor_2 = int(input("ingrese el numero 2:"))
        valor_3 = valor_1 // valor_2
        print("la division es:",valor_3)
