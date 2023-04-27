print("Recuperando o Acesso!")

#insira os minutos atuais
minutos = int(input("Por favor, insira a minutagem atual: "))
senha = 1
for i in range(1,minutos +1):
    senha *= i
print("A senha de acesso é: LIBERDADE{}.".format(senha))
