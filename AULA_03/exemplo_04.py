 # Programa Media
nome = input("Informe o mome do estudante: ")
n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
media = (n1 + n2)/ 2
if media >= 70:
    print(f"{nome}, você foi APROVADO, pois sua média foi {media:.2f}")
elif media >= 30 and media < 70:
    print(f"{nome}, você está de RECUPERAÇÃO, pois sua média foi {media:.2f}")
else:
    print(f"{nome}, você foi REPROVADO, pois sua média foi {media:.2f}")