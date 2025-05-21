#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

n = float(input("Digite a distancia da viagem em KM: "))
print(f"O preço da passagem será de R${n*0.5}" if n<=200
      else f"O preço da passagem será de R${n*0.45}" )