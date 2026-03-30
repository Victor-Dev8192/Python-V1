while True:

 CA = input (f'Valor do Cateto Adjacente: ').strip()

 CO = input (f'Valor do Cateto Oposto: ').strip()

 H = (int(CA)**2)+(int(CO)**2)

 print('Hipotenusa = {:.2f}'.format(H))