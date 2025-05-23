#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date   
current_Year= str(date.today())[:4]
current_Year = int(current_Year)
birth_Date= int(input("Digite o seu ano de nascimento: "))
print(f"Esse ano é seu ano de alistamento, SE ALISTE" if (current_Year-birth_Date)==18 else
      f"Seu ano de alistamento é somente em {birth_Date+18}" if (current_Year-birth_Date)<18 else
      f"Seu ano de alistamento JÁ PASSOU, e foi em {birth_Date+18}")