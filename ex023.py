#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
un = ['Unidade', 'Dezena', 'Centena', 'Milhar']

def divisor_Numeros(num):
    for i in range(len(num),0,-1):
        try:
            print(f"Você tem {num[i-(len(num))]} unidades de {un[i-1]}.")
        except:
            pass


n = list(input("Digite um número: "))
divisor_Numeros(n)