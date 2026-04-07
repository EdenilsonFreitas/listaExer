# Questao01
# salario = float(input("Digite-o seu salário: "))
# if salario <= 1903.98:
#     print("Isento de imposto de renda.")
# elif salario <= 2826.65: 
#     imposto = salario * 0.075
#     print(f"O imposto de renda a ser pago é: R$ {imposto:.2f}")
# elif salario <= 3751.05:
#     imposto = salario * 0.15
#     print(f"O imposto de renda a ser pago é: R$ {imposto:.2f}")
# elif salario <= 4664.68:
#     imposto = salario * 0.225
#     print(f"O imposto de renda a ser pago é: R$ {imposto:.2f}")
# else:
#     imposto = salario * 0.275
#     print(f"O imposto de renda a ser pago é: R$ {imposto:.2f}")


# Questao02

# ano = int(input("Digite o ano: "))
# if ano % 4 == 0 and ano % 100 != 0:
#     print("O ano é bissexto.")
# else:
#     print("O ano não é bissexto.")

# Questao03


# numero = int(input("Digite um número entre 1 e 10: "))
# if 1 <= numero <= 10:
#     print("O número digitado está DENTRO da faixa solicitada.")
# else:
#     print("O número digitado está FORA da faixa solicitada.")

# Questao04

# valor1 = float(input("Digite o primeiro valor: "))
# valor2 = float(input("Digite o segundo valor: "))
# if valor1 > valor2:
#     print(f"O maior valor é: {valor1}")

# elif valor2 > valor1:
#     print(f"O maior valor é: {valor2}")
# else:
#     print("Os valores são iguais.")

# Questao05



# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# if valor1 > valor2:
#     diferenca = valor1 - valor2
#     print(f"A diferença entre o maior valor e o menor valor é: {diferenca}")
# elif valor2 > valor1:
#     diferenca = valor2 - valor1
#     print(f"A diferença entre o maior valor e o menor valor é: {diferenca}")
# else:
#     print("Os valores são iguais. A diferença é 0.")

# Questao06


# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# valor3 = int(input("Digite o terceiro valor: "))
# valores = [valor1, valor2, valor3]
# valores.sort()
# print(f"Os valores digitados em ordem crescente são: {valores[0]}, {valores[1]} e {valores[2]}")

# Questao07



# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# valor3 = int(input("Digite o terceiro valor: "))
# ordem = input("Deseja ver os valores em ordem crescente ou decrescente? (crescente/decrescente): ").lower()
# valores = [valor1, valor2, valor3]
# if ordem == "crescente":
#     valores.sort()
#     print(f"Os valores em ordem crescente são: {valores[0]}, {valores[1]} e {valores[2]}")
# elif ordem == "decrescente":
#     valores.sort(reverse=True)
#     print(f"Os valores em ordem decrescente são: {valores[0]}, {valores[1]} e {valores[2]}")
# else:
#     print("Opção inválida. Por favor, escolha 'crescente' ou 'decrescente'.")


# Questao08


# lado1 = float(input("Digite o primeiro lado do triângulo: "))
# lado2 = float(input("Digite o segundo lado do triângulo: "))
# lado3 = float(input("Digite o terceiro lado do triângulo: "))
# if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
#     if lado1 == lado2 == lado3:
#         print("O triângulo é equilátero.")
#     elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
#         print("O triângulo é isósceles.")
#     else:
#         print("O triângulo é escaleno.")
# else:
#     print("Os valores digitados não podem formar um triângulo.")


