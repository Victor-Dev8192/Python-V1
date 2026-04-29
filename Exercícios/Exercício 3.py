import math as m

def Triangle_Number(x):
 return (int(x)*(int(x)+1))//2

def Op():
 Op = input('Lista de operações abaixo:\n\n1) Adição.\n\n2) Subtração.\n\n3) Multiplicação.\n\n4) Divisão.\n\n5) Exponenciação.\n\n6) Raíz Quadrada.\n\n7) Fatorial.\n\n8) Termial\n\n9) Números Iguais.\n\n10) Números Diferentes.\n\nOperação Escolhida = ').strip()
 try:
  x = float(input('\nPrimeiro valor? ').strip())
 except ValueError:
  print('Erro 1: Número inválido.')
  return
 
 y = None
 if Op in ('1', '2', '3', '4', '5','9','10'):

  try:
   y = float(input('\nSegundo valor? ').strip())
  except ValueError:
   print('Erro 1: Número inválido.')
   return

 match Op:

    case '1':

      Resultado = (x+y)
      return

    case '2':

      Resultado = (x-y)
      return

    case '3':

     Resultado = (x*y)
     return

    case '4':

      if y != 0:

        Resultado = (x/y)
        return

      else:

        print('\nErro 2: Divisão por zero é impossível.')
        return

    case '5':

     Resultado = (x**y)
     return

    case '6':

     Resultado = (m.sqrt(int(x)))
     return

    case '7':

     if x >= 0:

      Resultado = (m.factorial(int(x)))
      return

     else:
     
      print('\nErro 3: Fatorial de números negativos é impossível.')
      return

    case '8':

     Resultado = (Triangle_Number(x))
     return

    case '9':

     Resultado = (x==y)
     return

    case '10':

     Resultado = (x!=y)
     return

    case _:

     print('\nErro 4: Operação inválida e/ou indisponível.')
     return

while True:
 Op()
 Again = input('\nReiniciar? (Y/N): ').strip().upper()
 if Again != 'Y':
  print('\nTchau!')
  break