import math as m

x = float(input('Primeiro valor? (Se aplica a operações como Fatorial e Termial.) '))

y = float(input('Segundo valor? (Não se aplica a operações como Fatorial e Termial.) '))

Operation = input('Qual operação? (+,-,*,/, ^, Root, !, ?, =, Diff) ')

if (Operation == '+'):

    print(x+y)

elif (Operation == '-'):

    print(x-y)

elif (Operation == '*'):

    print(x*y)

elif (Operation == '^'):

    print(m.pow(x,y))

elif (Operation == 'Root'):

    print(m.sqrt(int(x)))
    print(m.sqrt(int(y)))

elif (Operation == '!'):

    print(m.factorial(int(x)))
    print(m.factorial(int(y)))

elif (Operation == '?'):

    print(int(x)*(int(x)+1)/2)
    print(int(y)*(int(y)+1)/2)

elif (Operation == '='):

    print(x==y)

elif (Operation == 'Diff'):

    print(x!=y)

elif (Operation == '/'):

    if y != 0:

        print(x/y)

    else:

        print('Erro Desconhecido: Divisão por zero é impossível.')

else:

  print('Operação inválida e/ou indisponível.')