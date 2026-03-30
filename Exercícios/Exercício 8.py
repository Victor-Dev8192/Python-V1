while True:

 CA = input (float(f'Valor do Cateto Adjacente: ')).strip()

 CO = input(float(f'Valor do Cateto Oposto: ')).strip()

 H = (CA**2)+(CO**2)

 print('Hipotenusa = {:.2f}'.format(H))