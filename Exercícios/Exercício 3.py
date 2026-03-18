import math as m

while True:

 x = float(input(f'Primeiro valor? (Se aplica a operações como Fatorial e Termial.) ').strip())

 y = float(input(f'Segundo valor? (Não se aplica a operações como Fatorial e Termial.) ').strip())

 Op = input(f'Qual operação? (+,-,*,/, ^, Root, !, ?, =, Diff) ').capitalize().strip()

 match Op:

    case '+' | 'Add' | 'Mais' | 'A' | 'M':

      print(x+y)
      print('Reiniciando...')

    case '-' | 'Minus' | 'Menos' | 'M':

      print(x-y)
      print('Reiniciando...')

    case '*' | 'Multiplicação' | 'Multiplication' | 'Multi' | 'M':

     print(x*y)
     print('Reiniciando...')

    case '/' | 'Division' | 'Divisão' | 'Diviz' | 'D':

      if y != 0:

        print(x/y)
        print('Reiniciando...')

      else:

        print(f'Erro 1: Divisão por zero é impossível.')
        print('Reiniciando...')

    case '^' | 'Exponenciação' | 'Exponente' | 'Power' | 'Ex' | 'P':

     print(x**y)
     print('Reiniciando...')

    case 'R' | 'Root' | 'Raiz':

     print(m.sqrt(int(x)))
     print(m.sqrt(int(y)))
     print('Reiniciando...')

    case '!' | 'Factorial' | 'Fatorial' | 'F':

     if x >= 0:

      print(m.factorial(int(x)))
      print('Reiniciando...')

     else:
     
      print(f'Erro 2: Fatorial de números negativos é impossível.')
      print('Reiniciando...')

     if y >= 0:
       
      print(m.factorial(int(y)))
      print('Reiniciando...')

     else:
      
      print(f'Erro 2: Fatorial de números negativos é impossível.')
      print('Reiniciando...')

    case '?' | 'Termial' | 'T':

     print(int(x)*(int(x)+1)/2)
     print(int(y)*(int(y)+1)/2)
     print('Reiniciando...')

    case '=' | 'Equal' | 'Igual' | 'E' | 'I':

     print(x==y)
     print('Reiniciando...')

    case 'Diferença' | 'DIferente' | 'Diff' | 'D':

     print(x!=y)
     print('Reiniciando...')

    case "Exit" | 'Sair' | 'E' | 'S':
   
     print(f'Encerrando...')
     break

    case _:

     print(f'Erro 3: Operação inválida e/ou indisponível.')
     print('Reiniciando...')