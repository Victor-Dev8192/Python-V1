import math as m

x = float(input(f'Primeiro valor? (Se aplica a operações como Fatorial e Termial.) '))

y = float(input(f'Segundo valor? (Não se aplica a operações como Fatorial e Termial.) '))

Op = input(f'Qual operação? (+,-,*,/, ^, Root, !, ?, =, Diff) ')

match Op:

    case '+':

      print(x+y)

    case '-':

      print(x-y)

    case '*':

     print(x*y)

    case '^':

     print(m.pow(x,y))

    case 'Root':

     print(m.sqrt(int(x)))
     print(m.sqrt(int(y)))

    case '!':

     if x >= 0:

      print(m.factorial(int(x)))

     else:
     
      print(f'Erro 1: Fatorial de números negativos é impossível.')

     if y >= 0:
       
      print(m.factorial(int(y)))

     else:
      
      print(f'Erro 1: Fatorial de números negativos é impossível.')

    case '?':

     print(int(x)*(int(x)+1)/2)
     print(int(y)*(int(y)+1)/2)

    case '=':

     print(x==y)

    case 'Diff':

     print(x!=y)

    case '/':

      if y != 0:

        print(x/y)

      else:

        print(f'Erro 2: Divisão por zero é impossível.')

    case _:

     print(f'Erro 3: Operação inválida e/ou indisponível.')