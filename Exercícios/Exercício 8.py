from math import hypot

while True:

 CA = input ('Valor do Cateto Adjacente: ').strip()

 CO = input ('Valor do Cateto Oposto: ').strip()

 H = hypot (int(CA), (int(CO)))

 print(f'Hipotenusa = {H:.2f}')