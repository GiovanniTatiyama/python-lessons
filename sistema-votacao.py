#Dia de live!
#informe a quantidade de votos que cada um dos 5 dias da semana teve
#verificar e exibir qual o dia da semana foi escolhido
print("Votação da livestrems!\nColoque o número de votos em cada um dos dias da semana.")
seg = int(input("Segunda-feira: "))
ter = int(input("Terça-feira: "))
qua = int(input("Quarta-feira: "))
qui = int(input("Quinta-feira: "))
sex = int(input("Sexta-feira: "))

if seg > ter and seg > qua and seg > qui and seg > sex:
    print("Segunda-feira venceu com {} votos!".format(seg))
elif ter > seg and ter > qua and ter > qui and ter > sex:
    print("Terça-feira venceu com {} votos!".format(ter))
elif qua > seg and qua > ter and qua > qui and qua > sex:
    print("Quarta-feira venceu com {} votos!".format(qua))
elif qui > seg and qui > ter and qui > qua and qui > sex:
    print("Quinta-feira venceu com {} votos!".format(qui))
elif sex > seg and sex > ter and sex > qua and sex > qui:
    print("Sexta-feira venceu com {} votos!".format(sex))
else: print("Deu empate, tente de novo!")
