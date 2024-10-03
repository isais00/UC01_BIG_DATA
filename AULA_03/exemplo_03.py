h = float(input("Informe a altura: "))
sexo = input("Informe M - para Masculino e F - para Feminino: ")
if sexo == "M" or sexo == "m":
    M = (72.7 * h) - 58
    print(f"O seu peso ideal é {M:.2f}")
elif sexo == "F" or sexo == "f":
    F = (62.1 * h) - 44.7
    print(f"O seu peso ideal é {F:.2f}")
else:
    print("Verifique o sexo informado")