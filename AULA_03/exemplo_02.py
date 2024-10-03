# if elif e else
idade = int(input("Informe a sua idade: "))
if idade < 18:
    print("Você é menor de idade")
elif idade == 18:
    print("Quase lá")
elif idade > 65:
    print("Acesso moderado")
else:
    print("Acesso liberado")

# Usando o conectivo and
# idade = int(input("Informe a sua idade: "))
# if idade < 18:
#    print("Você é menor de idade")
# elif idade == 18:
#    print("Quase lá")
# elif idade > 18 and < 65:
#    print("Acesso liberado")
# else:
#    print("Acesso moderado")