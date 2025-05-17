# A cada 2m² de parede precisam de 1 litro de tinta para serem pintados
largura_Parede = float(input("Digite a largura da parede em metros: "))
altura_Pàrede = float(input("Digite a altura da parede em metros: "))

print(f"Se sua parede tem dimensão de {largura_Parede}m X {altura_Pàrede}m , você precisará de {largura_Parede*altura_Pàrede:.2f}l de tinta.")