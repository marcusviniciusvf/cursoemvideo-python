#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input("Digite seu nome: ")).lower().split(" ")
print(f"""Primeiro nome é {n[0].capitalize()}
Ultimo nome é {n[-1].capitalize()}""")