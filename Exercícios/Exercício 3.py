import math as m

def Triangle_Number(x):
 return (int(x)*(int(x)+1))//2

def Number_Format(n):
   
  if n == 0:
   return '0'
 
  elif abs(n) >= 1e12:
   return f'{n:.2e}'
  
  elif abs(n) <= 1e-3:
   return f'{n:,.2e}'
  
  else:
   return f'{n:,.10f}'.rstrip('0').rstrip('.')

def Op():
 Op = input('Lista de operações abaixo:\n\n1) Adição.\n\n2) Subtração.\n\n3) Multiplicação.\n\n4) Divisão.\n\n5) Exponenciação.\n\n6) Raíz De Qualquer Base.\n\n7) Logaritmo De Qualquer Base.\n\n8) Fatorial.\n\n9) Termial\n\n10) Números Iguais.\n\n11) Números Diferentes.\n\nOperação Escolhida = ').strip()[0]
 try:
  x = float(input('\nPrimeiro valor? ').strip())
 except ValueError:
  print('\nErro 1: Número inválido.')
  return
 
 y = None
 if Op in ('1', '2', '3', '4', '5','6','7','10','11'):

  try:
   y = float(input('\nSegundo valor? ').strip())
  except ValueError:
   print('\nErro 1: Número inválido.')
   return

 match Op:

  case '1':

   Resultado = (x+y)
   print('\n' + Number_Format(Resultado))
   return

  case '2':

   Resultado = (x-y)
   print('\n' + Number_Format(Resultado))
   return

  case '3':

   Resultado = (x*y)
   print('\n' + Number_Format(Resultado))
   return

  case '4':

    if y != 0:

     Resultado = (x/y)
     print('\n' + Number_Format(Resultado))
     return

    else:

     print('\nErro 2: Divisão Por Zero É Impossível.')
     return

  case '5':

   Resultado = (x**y)
   print('\n' + Number_Format(Resultado))
   return

  case '6':
   
   try:

    Resultado = (x**(1/y))
    print('\n' + Number_Format(Resultado))
   
   except ValueError:

    print('\nErro 1: Número Inválido.')

    return
  
  case '7':
   
   try:
   
    Resultado = (m.log(x,y))
    print('\n' + Number_Format(Resultado))

   except ValueError:

    print('\nErro 1: Número Inválido.')

    return

  case '8':

   if x >= 0:

    Resultado = (m.factorial(int(x)))
    print('\n' + Number_Format(Resultado))
    return

   else:
     
    print('\nErro 3: Fatorial De Números Negativos É Impossível.')
    return

  case '9':

   Resultado = (Triangle_Number(int(x)))
   print('\n' + Number_Format(Resultado))
   return

  case '10':

   Resultado = (x==y)
   print('\n', Resultado)
   return

  case '11':

   Resultado = (x!=y)
   print('\n', Resultado)
   return

  case _:

   print('\nErro 4: Operação Inválida E/Ou Indisponível.')
   return

while True:
 Op()
 print()
 Again = input('Reiniciar? (S/N): ').upper().strip()[0]
 if Again != 'S':
  print('\nTchau!\n')