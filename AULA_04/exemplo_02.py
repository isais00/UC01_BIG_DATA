try:
    nomep = input("Insira o nome do produto: ")
    quantp = int(input("Insira a quantidade dos produtos: "))
    preco = float(input("Insira o preço do produto por unidade: "))
except ValueError:
    print("Verifique os valores informados")
else:
    total = (quantp*preco)
    print(f"Ovalor total a ser pago é R$ {total:.2f}")
    if quantp <= 5:
        print("Seu desconto foi de 2%, total a pagar: ",(total*0.98))
    elif quantp > 5 and quantp <= 10:
        print("Seu desconto foi de 3%, total a pagar: ",(total*0.97))
    else:
        print("Seu desconto foi de 10%, total a pagar: ",(total*0.95))