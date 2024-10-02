# Calcule o valor de uma prestacao em atraso
prestacao = float(input("Insira o valor da prestação: "))
taxa = float(input("Insira a taxa: "))
tempo = float(input("Isira o tempo em meses: "))
valor_final = prestacao + (prestacao*(taxa/100)*tempo)
print(F"O valor em atraso é de R$ {valor_final:.2F}")