# Questao01
"""
Escreva um programa que leia dois valores que representem o início
e o fim de um intervalo. O programa deverá ler um terceiro valor
digitado e verificar se este terceiro valor está dentro do intervalo ou
fora. Caso esteja fora do intervalo, deverá informar se está na parte
inferior ou superior do intervalo.
"""
# num1 = int(input("Digite o início do intervalo: "))
# num2 = int(input("Digite o fim do intervalo: "))
# num3 = int(input("Digite o terceiro valor: "))

# if num3 < num1:
#     print("O terceiro valor está abaixo do intervalo.")
# elif num3 > num2:
#     print("O terceiro valor está acima do intervalo.")
# else:
#     print("O terceiro valor está dentro do intervalo.")

#Questao 02

"""
Escreva um programa que sempre escolhe o menor caminho a ser percorrido pelo
usuário em função do local onde ele está e as opções de caminho a serem seguidas. O
usuário sempre parte do ponto A (Início) em direção ao Fim (D, E, F ou G). O usuário
deverá fornecer as distância entre os pontos e o programa deverá apresentar o caminho
a ser percorrido e a distância percorrida. Utilizar apenas estruturas condicionais.
"""

# AB = float(input("Distaância de A Até B: "))
# AC = float(input("Distaância de A Até C: "))
# BD = float(input("Distaância de B Até D: "))
# BE = float(input("Distaância de B Até E: "))
# CF  = float(input("Distância de C Até F: "))
# CG = float(input("Distância de C Até G: "))
# caminho1 = AB +BD
# caminho2 = AB + BE
# caminho3 = AC + CF
# caminho4 = AC + CG
# # Inicialmente assume o primeiro como menor
# menor = caminho1
# rota = "A -> B -> D"

# # Comparações usando apenas if
# if caminho2 < menor:
#     menor = caminho2
#     rota = "A -> B -> E"

# if caminho3 < menor:
#     menor = caminho3
#     rota = "A -> C -> F"

# if caminho4 < menor:
#     menor = caminho4
#     rota = "A -> C -> G"

# # Saída
# print("\nResultado:")
# print("Caminho percorrido:", rota)
# print("Distância percorrida:", menor)

