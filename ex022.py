#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome: ")).strip()
print(f"""Seu nome MAIUSCULO é : {nome.upper()}
Seu nome minúsculo é: {nome.lower()}
Seu nome tem {len(nome)-nome.count(' ')} letras
Seu primeito nome tem {nome.find(' ')} letras""")