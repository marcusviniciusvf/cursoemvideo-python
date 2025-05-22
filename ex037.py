#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
#  qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
#Conversor de Bases Numéricas

numero = int(input("Digite um número inteiro: "))
menu_Conversao = 0
menu_Conversao = int(input("[1] para conversão em BINARIO\n[2] para conversão em OCTAL\n[3] para conversão em HEXADECIMAL" while menu_Conversao not in [1,2,3] else ""))

print(menu_Conversao)