#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER
#Classificando Atletas
from datetime import date   
current_Year= str(date.today())[:4]
birth_Date = int(input("Digite seu ano de nascimento: "))
current_Age = int(current_Year)-birth_Date
print('Sua categoria é ', end='')
print("MIRIM" if current_Age<=9 else
      "INFANTIL" if current_Age>9 and current_Age<=14 else
      "JÚNIOR" if current_Age>14 and current_Age<=19 else
      "SÊNIOR" if current_Age>19 and current_Age<=25 else
      "MASTER")