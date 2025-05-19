#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#  e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

rent_Days = int(input("Por quantos dias o carro foi alugado? "))
rent_Kilometers = float(input("Quantos KM foram rodados durante o aluguel? "))

rent_Price = (rent_Days*60) + (rent_Kilometers*0.15)

print(f"O valor do aluguel para {rent_Days} dias e {rent_Kilometers}KM rodados é de R${rent_Price}")