Usuarios = ["Alessandro", "Pedro", "Luis", "Maria", "Roberta"]
senhas = ["1234", "14@05","3317", "4455", "4444"]
usuario = input("Informe o nome do usuário: ")
for i in range(len(Usuarios)):
    if Usuarios[i] == usuario:
       resp = "Usuário encontrado!"
       resp_01  = input("Digite a senha: ")
       break
    else:
        resp = "Usuário não encontrado!"
print(resp)