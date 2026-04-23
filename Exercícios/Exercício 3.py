import math as m

def Triangle_Number(x):
 return (int(x)*(int(x)+1))//2

def Op():
 print ('Operações disponíveis: +,-,*,/, ^, Root, !, ?, =, Diff')
 Op = input('\nQual operação? ').capitalize().strip()
 try:
  x = float(input('\nPrimeiro valor? ').strip())
 except ValueError:
  print('Erro 1: Número inválido.')
  return
 
 y = None
 if Op in ('+','Add','Mais','A','M+','-','Minus','Menos','M-','*','Multiplicação','Multiplication','Multi','M','/','Divisão','Division','Diviz','D+','^','Exponenciação','Exponente','Power','Ex','P','=','Equal','Igual','E+','I','!=','Diferença','Diferente','Diff','D'):

  try:
   y = float(input('\nSegundo valor? ').strip())
  except ValueError:
   print('Erro 1: Número inválido.')
  return

 match Op:

    case '+' | 'Add' | 'Mais' | 'A' | 'M+':

      print(x+y)
      return

    case '-' | 'Minus' | 'Menos' | 'M-':

      print(x-y)
      return

    case '*' | 'Multiplicação' | 'Multiplicacao' | 'Multiplication' | 'Multi' | 'M':

     print(x*y)
     return

    case '/' | 'Divisão' | 'Divisao' | 'Division' | 'Diviz' | 'D+':

      if y != 0:

        print(x/y)
        return

      else:

        print('Erro 2: Divisão por zero é impossível.')
        return

    case '^' | 'Exponenciação' | 'Exponenciacao' | 'Exponente' | 'Power' | 'Ex' | 'P':

     print(x**y)
     return

    case 'R' | 'Root' | 'Raíz' | 'Raiz':

     print(m.sqrt(int(x)))
     return

    case '!' | 'Factorial' | 'Fatorial' | 'F':

     if x >= 0:

      print(m.factorial(int(x)))
      return

     else:
     
      print('Erro 3: Fatorial de números negativos é impossível.')
      return

    case '?' | 'Triangle' | 'Termial' | 'T':

     print(Triangle_Number(x))
     return

    case '=' | 'Equal' | 'Igual' | 'E+' | 'I':

     print(x==y)
     return

    case '!=' | 'Diferença' | 'Diferenca' | 'DIferente' | 'Diff' | 'D':

     print(x!=y)
     return

    case _:

     print('Erro 4: Operação inválida e/ou indisponível.')
     return

while True:
 Op()
 Again = input('\nReiniciar? (Y/N): ').strip().upper()
 if Again != 'Y':
  print('Tchau!')
  break