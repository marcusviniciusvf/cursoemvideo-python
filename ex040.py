#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO
#Aquele clássico da Média
notas_Aluno = []
qtd_Notas = 2
add_Notas = [notas_Aluno.append(int(input(f"Digite a nota {i+1}: "))) for i in range(qtd_Notas)]

print("APROVADO" if (sum(notas_Aluno)/qtd_Notas)>=7 else
      "RECUPERAÇÃO" if (sum(notas_Aluno)/qtd_Notas)<7 and (sum(notas_Aluno)/qtd_Notas)>=5 else
       "REPROVADO" )