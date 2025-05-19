#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

nome_Alunos = []

qtd_Alunos = int(input("Digite a quantidade de alunos a serem sorteados: "))
for i in range(qtd_Alunos):
    add_Aluno = str(input(f"Digite o nome do aluno {i+1}:"))
    nome_Alunos.append(add_Aluno)



print(f"O aluno escolhido foi: {random.choice(nome_Alunos)}")