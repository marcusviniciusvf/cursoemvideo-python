#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math 

a = float(input("Digite o ângulo: "))
a_sin = math.sin(math.radians(a))
a_cos = math.cos(math.radians(a)) 
a_tan = math.tan(math.radians(a))

print(f"O seno é {a_sin:.2f}, cosseno é {a_cos:.2f}, tangente é {a_tan:.2f}")