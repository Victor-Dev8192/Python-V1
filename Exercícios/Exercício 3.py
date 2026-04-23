import math as m

def Op():
 print ('Available Ops: +,-,*,/, ^, Root, !, ?, =, Diff')
 Op = input(f'\nQual operação? ').capitalize().strip()
 try:
  x = float(input(f'Primeiro valor? ').strip())
 except ValueError:
  print('Erro 1: Número inválido.')
  return
 
 y = None
 if Op in ('+','Add','Mais','A','M+','-','Minus','Menos','M-','*','Multiplicação','Multiplication','Multi','M','/','Divisão','Division','Diviz','D+','^','Exponenciação','Exponente','Power','Ex','P','=','Equal','Igual','E+','I','!=','Diferença','Diferente','Diff','D'):

  try:
   y = float(input(f'Segundo valor? ').strip())
  except ValueError:
   print('Erro 1: Número inválido.')
  return

while True:

 match Op:

    case '+' | 'Add' | 'Mais' | 'A' | 'M+':

      print(x+y)
      print('Reiniciando...')

    case '-' | 'Minus' | 'Menos' | 'M-':

      print(x-y)
      print('Reiniciando...')

    case '*' | 'Multiplicação' | 'Multiplication' | 'Multi' | 'M':

     print(x*y)
     print('Reiniciando...')

    case '/' | 'Divisão' | 'Division' | 'Diviz' | 'D+':

      if y != 0:

        print(x/y)
        print('Reiniciando...')

      else:

        print(f'Erro 2: Divisão por zero é impossível.')
        print('Reiniciando...')

    case '^' | 'Exponenciação' | 'Exponente' | 'Power' | 'Ex' | 'P':

     print(x**y)
     print('Reiniciando...')

    case 'R' | 'Root' | 'Raiz':

     print(m.sqrt(int(x)))
     print('Reiniciando...')

    case '!' | 'Factorial' | 'Fatorial' | 'F':

     if x >= 0:

      print(m.factorial(int(x)))
      print('Reiniciando...')

     else:
     
      print(f'Erro 3: Fatorial de números negativos é impossível.')
      print('Reiniciando...')

    case '?' | 'Termial' | 'T':

     print(int(x)*(int(x)+1)/2)
     print(int(y)*(int(y)+1)/2)
     print('Reiniciando...')

    case '=' | 'Equal' | 'Igual' | 'E+' | 'I':

     print(x==y)
     print('Reiniciando...')

    case '!=' | 'Diferença' | 'DIferente' | 'Diff' | 'D':

     print(x!=y)
     print('Reiniciando...')

    case "Exit" | 'Sair' | 'E' | 'S':
   
     print(f'Encerrando...')
     break

    case _:

     print(f'Erro 4: Operação inválida e/ou indisponível.')
     print('Reiniciando...')