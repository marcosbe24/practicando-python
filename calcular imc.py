def calcular_imc():
    kilo = float(input("ingresar tu peso:"))
    altura = float(input("INGRESE SU ESTATURA:"))
    return kilo / (altura*altura)

resultado = calcular_imc()
print(int(resultado))