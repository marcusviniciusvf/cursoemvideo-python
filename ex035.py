#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#Analisando Triângulo v1.0

lados = [float(input(f"Digite o lado numero {i+1}: ")) for i in range(3)]

print("Os lados PODEM formar um triângulo" if lados[0]+lados[1]>lados[2] and lados[1]+lados[2]>lados[0] and lados[0]+lados[2]>lados[1]
      else "Os lados NÃO PODEM formar um triângulo")
