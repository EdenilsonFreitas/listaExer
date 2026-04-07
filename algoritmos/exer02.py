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
"""
Escreva um programa que solicita o valor de um ano ao usuário, em seguida informa
se o ano fornecido é ou não bissexto. [Dica: um ano é bissexto se é divisível por 4,
mas não por 100. Para que um número X seja considerado divisível por um número
Y é preciso que o resto da divisão de X por Y seja igual a ZERO].
"""
ano = int(input("Digite o ano: "))
if ano % 4 == 0 and ano % 100 != 0:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
