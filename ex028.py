#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
rand_Num = randint(0,5)
user_Input = int(input("Digite o numero que estou pensando de 0 a 5: "))
print(f'Voce Ganhou, eu estava pensando em {rand_Num}' if user_Input==rand_Num else f'Voce perdeu, eu estava pensando em {rand_Num}')

