#ex038  Comparando números
#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
print(f"{n1} (PRIMEIRO) é maior que {n2}" if n1>n2 else f"{n2} (SEGUNDO) é maior que {n1}" if n2>n1 else f"Os numeros são iguais, {n1}")