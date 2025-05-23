#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer
#e peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal.
#037 Conversor de Bases Numéricas
num = int(input("Digite seu numero: "))
opcao = int(input("""[1] para BINARIO
[2] para OCTAL
[3] para HEXADECIMAL
Digite sua opção: """))
print(bin(num)[2:] if opcao==1 else oct(num)[2:] if opcao==2 else hex(num)[2:] if opcao==3 else 'Opcao invalida')