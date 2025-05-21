#Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

car_Speed = int(input("Digite a velocidade do carro em Km/h: "))
print("Tudo certo, dirija com segurança" if car_Speed<=80 
      else f"MULTADO! Você está {car_Speed-80}Km/h acima do limite de 80Km/h  \nSua multa é no valor de R${(car_Speed-80)*7}")