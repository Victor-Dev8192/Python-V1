while True:
 
 h = float(input('Altura da parede em metros? '))

 w = float(input('Largura da parede em metros? '))

 a = h + w

 p1 = a*8.5

 p2 = a*4.25

 p3 = a*2.125

 print('1 demão = {}m² | 2 demãos = {}m² | 3 demãos = {}m²'.format(p1, p2, p3))