#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime

ano = int(input("Digite o ano que deseja descobrir se é bissexto (0 para o ano atual): "))
if ano == 0:
    ano = datetime.date.today().year

if ano%4==0 and ano%100!=0 or ano%400==0:
    print(f"{ano} é bissexto.")
else:
    print(f"{ano} não é bissexto")
