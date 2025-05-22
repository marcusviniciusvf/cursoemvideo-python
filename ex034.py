#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
# Aumentos múltiplos

salario = float(input("Digite seu salário: "))
print(f"Quem ganhava R${salario} passa a ganhar R${salario*1.15}" if salario<=1250
      else f"Quem ganhava R${salario} passa a ganhar R${salario*1.10}")