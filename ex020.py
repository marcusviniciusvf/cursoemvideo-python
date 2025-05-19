#Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random 
nome_Alunos = []
ordem_Alunos = []

qtd_Alunos = int(input("Digite a quantidade de alunos a serem sorteados: "))
for i in range(qtd_Alunos):
    add_Aluno = str(input(f"Digite o nome do aluno {i+1}:"))
    nome_Alunos.append(add_Aluno)

for _ in range(len(nome_Alunos)):
    sel_Aluno = random.choice(nome_Alunos)
    ordem_Alunos.append(sel_Aluno)
    nome_Alunos.remove(sel_Aluno)

print(f"A ordem será: {ordem_Alunos}")