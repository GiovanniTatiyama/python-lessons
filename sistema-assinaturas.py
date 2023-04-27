print("Olá, Bem-vindo ao sistema! Assinaturas:\nBasic digite: 1\nSilver digite: 2\nGold digite: 3\nPlatinum digite: 4")

#Receba o tipo de assinatura do cliente
nivel = int(input("Qual é sua assinatura? "))
#Receba o faturamento anual do cliente
faturamento = float(input("Qual foi seu faturamento anual? "))
#Calcular e exibir o valor do bônus que o cliente deve pagar

#Nivel Basic
if nivel == 1:
    pag = faturamento * 0.3
    print("o valor do bônus a ser pago é de R${:.2f}".format(pag))

#Nivel Silver
elif nivel == 2:
    pag = faturamento * 0.2
    print("o valor do bônus a ser pago é de R${:.2f}".format(pag))

#Nivel Gold
elif nivel == 3:
    pag = faturamento * 0.1
    print("o valor do bônus a ser pago é de R${:.2f}".format(pag))

#Nivel Platinum
elif nivel == 4:
    pag = faturamento * 0.05
    print("o valor do bônus a ser pago é de R${:.2f}".format(pag))
