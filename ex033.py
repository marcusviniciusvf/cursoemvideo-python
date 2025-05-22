#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
#Maior e menor valores

numeros = [int(input(f"Digite o {i+1}o numero: ")) for i in range(3)]

print(f"""O menor valor digitado foi {min(numeros)}
O maior valor digitado foi {max(numeros)}""")