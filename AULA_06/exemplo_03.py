nomes = []
medias = []
resp = "S"
while resp == "S" or resp == "s":
    nomes.append(input("Informe o nome do estudante: "))
    medias.append(float(input("Iforme a média do estudante: ")))
    resp = input("Deseja continuar(S/N)? ")
for i in range(len(medias)):
    print(i, " - ", nomes[i], " - ", medias[i])
maior_media = max(medias)
pos = medias.index(maior_media)
print(f"{nomes[pos]}, você possui a maior média.")
print(f"A média da turma é: {(sum(medias)/len(medias)):.1f}")
print(f"A menor média é: {min(medias)}")
print(f"O total das médias é: {sum(medias):.2f}")
print(f"A amplitude da média da turma é: {max(medias)-min(medias):.2f}")
medias.sort()
print(medias)