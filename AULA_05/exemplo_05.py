soma_m = 0
soma_f = 0
maior = 0
for i in range(5):
    idade = int(input("Informe a idade: "))
    sexo = input("Insira 'F' para FEMININO e 'M' para MASCULINO: ")
    if idade > maior:
        maior = idade
print("A maior idade é: ",maior)