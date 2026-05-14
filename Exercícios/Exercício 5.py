while True:
 
 h = float(input('Altura da parede em metros? '))

 w = float(input('Largura da parede em metros? '))

 a = h + w

 p1 = a*8.5

 p2 = a*4.25

 p3 = a*2.125

 print(f'1 demão = {p1:.2f}L/m² | 2 demãos = {p2:.2f}L/m² | 3 demãos = {p3:.2f}L/m²')
 print('Reiniciando...')