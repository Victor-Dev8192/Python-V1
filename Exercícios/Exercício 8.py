from math import hypot

while True:

 CA = input (f'Valor do Cateto Adjacente: ').strip()

 CO = input (f'Valor do Cateto Oposto: ').strip()

 H = hypot (int(CA), (int(CO)))

 print('Hipotenusa = {:.2f}'.format(H))