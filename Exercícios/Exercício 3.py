import math as m

x = float(input('Primeiro valor? (Se aplica a operações como Fatorial e Termial.) '))

y = float(input('Segundo valor? (Não se aplica a operações como Fatorial e Termial.) '))

Operation = input('Qual operação? (+,-,*,/, ^, Root, !, ?, OR, NOR) ')

if (Operation == '+'):

    print(x+y)

elif (Operation == '-'):

    print(x-y)

elif (Operation == '*'):

    print(x*y)

elif (Operation == '^'):

    print(m.pow(x,y))

elif (Operation == 'Root'):

    print(m.sqrt(x,y))

elif (Operation == '!'):

    print(m.factorial(x))

elif (Operation == '?'):

    print(x*(x+1)/2)

elif (Operation == 'OR'):

    print(x=y)

elif (Operation == 'NOR'):

    print(x!=y)

elif (Operation == '/'):

    if y != 0:

        print(x/y)

    else:

        print('Erro Desconhecido: Divisão por zero é impossível.')

else:

  print('Operação inválida e/ou indisponível.')