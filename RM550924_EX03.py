#A escola de inglês JoWell Sant’ana

#Alunos pares
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")

totalNotas = 0
for par in range(2,51,2):
    notas = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(par)))
    totalNotas += notas
    mediaPar = totalNotas / 25 #metade da sala aqui
print("A nota média da metade PAR é {}!".format(mediaPar))

#Alunos impares
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")

totalNotas = 0
for impar in range(1,50,2):
    notas = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(impar)))
    totalNotas += notas
    mediaImpar = totalNotas / 25 #metade da sala aqui
print("A nota média da metade ÍMPAR é {}!".format(mediaImpar))

#Comparando qual média de nota foi maior
if mediaPar > mediaImpar:
    print("A nota média dos alunos PARES foi maior!")
elif mediaImpar > mediaPar:
    print("A nota média dos alunos ÍMPARES foi maior!")
else:
    print("A nota média dos alunos PARES E ÍMPARES foi igual!")
