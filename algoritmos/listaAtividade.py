import math

# Questão 01.
# entrada dos dados
# num1 = float(input("Digite o primeiro valor: "))
# num2 = float(input("Digite o segundo valor: "))

# soma = num1 + num2
# subtracao = num1 - num2
# multiplicacao = num1 * num2
# divisao = num1 / num2

#Questão 02
# print(f"A soma de {num} + {num} é: {soma}")
# print(f"A subtração de {num1} - {num2} é: {subtracao}")
# print(f"A multiplicação de {num1} * {num2} é: {multiplicacao}")
# print(f"A divisão de {num1} / {num2} é: {divisao}")


# num3 = float(input ("Digite a temperatura: "))

# temperatura = num3 * 1.8 + 32 

# print(f"A temperatura em celsius para fahreiheit: {temperatura} ºF")

# Questão 03
# raio = float(input("Digite o raio do Circulo: "))
# area = math.pi * raio**2
# print(f"Área do Circulo: {area:.2f}")
# Questão 04

# base = float(input("Digite a base do Triângulo: "))
# altura = float(input("Digite a altura do Triangulo: "))

# area = (base*altura)/2

# print(f"Área do Triangulo: {area:.2f}")
# Questão 05
"""
Volume da Esfera: Solicite ao usuário um valor do raio de uma esfera, calcule seu
volume e exiba o resultado do cálculo.
"""
# raio = float(input("Digite o raio da Esfera: "))
# volume = (4/3)* math.pi*raio ** 3
# print(f"Volume da Esfera: {volume:.2f}")


# Questão 06
"""
Calculadora de Média Aritmética: Solicite ao usuário para que ele insira três
valores de notas, realize o cálculo da média aritmética e em seguida exiba os três
valores digitados pelo usuário e o resultado do cálculo.
"""
# valor1 = float(input("Digite a primeira nota: "))
# valor2 = float(input("Digite a segunda nota: "))
# valor3 = float(input("Digite a terceira nota: "))
# media = (valor1+valor2+valor3) /3
# print(f"As notas digitadas foram: {valor1}, {valor2} e {valor3}")
# print(f"A média aritmética das notas é: {media:.2f}")


# Questão 07
"""
Calculadora de Média Ponderada: Solicite ao usuário para que ele insira os
valores de 4 notas e seus respectivos pesos, em seguida realize o cálculo da média
pondera e exiba o resultado do cálculo.
"""
# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))
# n3 = float(input("Digite a terceira nota: "))
# n4 = float(input("Digite a quarta nota: "))
# p1 = float(input("Digite o peso da primeira nota: "))
# p2 = float(input("Digite o peso da segunda nota: "))
# p3 = float(input("Digite o peso da terceira nota: "))
# p4 = float(input("Digite o peso da quarta nota: "))
# media_ponderada = (n1*p1 + n2*p2 + n3*p3 + n4*p4) / (p1+p2+p3+p4)
# print(f"A média ponderada das notas é: {media_ponderada:.2f}")



# Questão 08
"""
Equação de Segundo Grau: Solicite ao usuário os valores de “a”, “b”, “c” e “x”, em
seguida resolva uma equação quadrática do tipo y = ax2 + bx + c e exiba o valor
de y para o usuário.
"""
# a = float(input("Digite o valor de a: "))
# b = float(input("Digite o valor de b: "))
# c = float(input("Digite o valor de c: "))
# x = float(input("Digite o valor de x: "))
# y = a*x**2 + b*x + c
# print(f"O valor de y para a equação quadrática é: {y:.2f}")


# Questão 09

"""
Calculadora de IMC: Solicite ao usuário os valores de peso (kg) e altura (m),
calcule o índice de massa corporal (IMC), sabendo que IMC = , em seguida

exiba o valor do IMC calculado.
"""
# peso = float(input("Digite o peso em kg: "))
# altura = float(input("Digite a altura em metros: "))
# imc = peso / altura**2
# print(f"O índice de massa corporal (IMC) é: {imc:.2f}")

# Questão 10
"""
10.Tabuada: Solicite ao usuário um valor numérico, em seguida, exiba a tabuada de
um número específico (por exemplo, 5). O programa deverá ter como saída:
5x1 = 5; 5x2 = 10; 5x3 = 15; 5x4 = 20; 5x5 = 25; 5x6 = 30; 5x7 = 35; 5x8 = 40; 5x9
= 45; 5x10 = 50;
"""
# v1 = int(input("Digite um valor numerico: "))
# for i in range(1, 11):
#     resultado = v1 * i
#     print(f"{v1} x {i} = {resultado}")




# Questão 11
"""
11.Conversão de Segundos para o Formato HORA:MINUTO:SEGUNDO: Solicite
ao usuário um valor numérico correspondente à quantidade de segundos, em
seguida converta o valor para o formato de HORA:MINUTO:SEGUNDO.
"""

# segundos = int(input("Digite a quantidade de segundos: "))
# horas = segundos // 3600
# minutos = (segundos % 3600) // 60
# segundos_restantes = segundos % 60
# print(f"{horas:02d}:{minutos:02d}:{segundos_restantes:02d}")

