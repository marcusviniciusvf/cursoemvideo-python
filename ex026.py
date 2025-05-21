#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

nome = '  Amanda'.lower().strip()
cont_A = 0
last_Pos = 0

for _ in range(len(nome)):
    if cont_A==0 and nome[_]== 'a':
        print(f"A primeira ocorrência é na posição {_}")
        cont_A=+1
    elif nome[_]== 'a':
        cont_A+=1
        last_Pos = _

print(f"""A ultima ocorrência é na posição {last_Pos}
A letra "A" apareceu {cont_A} vezes""")


""" FORMA MOSTRADA NO VIDEO
frase = str(input('Digite uma frase: ')).upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))"""