#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
# Aprovando Empréstimo
valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário: "))
tempo = float(input("Quantos anos de financiamento? "))
parcela = valor/(tempo*12)
print(f"Para pagar uma casa de R${valor} em {tempo} anos, o valor da parcela será de R${parcela:.2f}")
print("Emprestimo APROVADO" if parcela<(salario*0.3)
      else "Emprestimo NEGADO")