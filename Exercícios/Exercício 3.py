import math as m

x = float(input('Primeiro valor? (Se aplica a operações como Fatorial e Termial.) '))

y = float(input('Segundo valor? (Não se aplica a operações como Fatorial e Termial.) '))

Op = input('Qual operação? (+,-,*,/, ^, Root, !, ?, =, Diff) ')

if (Op == '+'):

    print(x+y)

elif (Op == '-'):

    print(x-y)

elif (Op == '*'):

    print(x*y)

elif (Op == '^'):

    print(m.pow(x,y))

elif (Op == 'Root'):

    print(m.sqrt(int(x)))
    print(m.sqrt(int(y)))

elif (Op == '!'):

    print(m.factorial(int(x)))
    print(m.factorial(int(y)))

elif (Op == '?'):

    print(int(x)*(int(x)+1)/2)
    print(int(y)*(int(y)+1)/2)

elif (Op == '='):

    print(x==y)

elif (Op == 'Diff'):

    print(x!=y)

elif (Op == '/'):

    if y != 0:

        print(x/y)

    else:

        print('Erro Desconhecido: Divisão por zero é impossível.')

else:

  print('Operação inválida e/ou indisponível.')