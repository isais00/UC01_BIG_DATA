try:
    nome = input("Insira o nome do empregado: ")
    idade = int(input("Insira a idade do empregado: "))
    ano_e = int(input("Insira quantos anos o empregado tem na empresa: "))
except ValueError:
    print("Verifique os dados informados")
else:
    if idade >= 65:
        print("Apto a Aposentadoria")
    elif ano_e >= 30:
        print("Apto a Aposentadora")
    elif idade >= 60 and ano_e >= 25:
        print("Apto a Aposentadora")
    else:
        print('Inapto a Aposentadoria')