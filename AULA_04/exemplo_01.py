try:
    n1 = int(input("Infrome um número inteiro: "))
    n2 = int(input("Informe um segundo número inteiro: "))
except ValueError:
    print("Verifique a entrada de dados!")
else:
    try:
        d = n1/n2
    except ZeroDivisionError:
        print("Não é possível dividir por zero!")
    else:
        print(d)