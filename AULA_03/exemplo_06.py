nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
peso = float(input("Insira seu peso: "))
dormir = int(input("Insira quanto tempo você dormiu nas útimas 24h: "))
if (idade >= 16 and idade < 60) and (peso < 50) and (dormir > 6):
    print("Você pode doar sangye")
else:
    print("Você não pode doar sangue")