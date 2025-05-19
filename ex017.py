#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
cat_Oposto = float(input("Digite o valor do cateto oposto: "))
cat_Adjacente = float(input("Digite o valor do cateto adjacente: "))

h = ((cat_Oposto**2) + (cat_Adjacente**2))**(1/2)

print(f"A hipotenusa é {h:.2f}")