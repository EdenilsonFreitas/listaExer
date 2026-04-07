#Questã01o
"""
Escreva um algoritmo que leia o valor de um número inteiro digitado
pelo usuário e armazene esse valor em uma variável;
■ O algoritmo deve verificar se o valor digitado é um número positivo.
■ Se o valor digitado for maior do que ZERO o programa deve escrever na tela
“O número é positivo!”

"""
# nun1 = int(input("Digite o número inteiro: "))
# if nun1 > 0:
#     print("O número é positivo!")


# Questao 02

"""
Escreva um algoritmo que solicite ao usuário o valor de duas notas e
armazene o resultado em duas variáveis diferentes;
■ Calcule o resultado da média desses valores;
■ Imprima “Você está em RECUPERAÇÃO!!!” caso o resultado da média seja
maior ou igual a 30 e menor do que 70.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a seguanda nota: "))
media = nota1+nota2/2
if(30 <= media < 70):
    print("Você está de recuperação!")