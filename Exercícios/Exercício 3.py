import math as m

x = int(input('Primeiro valor? (Se aplica a operações como Fatorial e Termial.) '))

y = int(input('Segundo valor? (Não se aplica a operações como Fatorial e Termial.) '))

Operation = input('Qual operação? (+,-,*,/, ^, √, !, ?, Nome encurtado da operação.) ')

if (Operation == '+'):

    print(x+y)

elif (Operation == '-'):

    print(x-y)

elif (Operation == '*'):

    print(x*y)

elif (Operation == '^'):

    print(m.pow(x,y))

elif (Operation == '√'):

    print(m.sqrt(x,y))

elif (Operation == '!'):

    print(m.factorial(x))

elif (Operation == '?'):

    print(x*(x+1)/2)

elif (Operation == '/'):

    if y != 0:

        print(x/y)

    else:

        print('Erro Desconhecido: Divisão por zero é impossível.')

else:

  print('Operação inválida e/ou indisponível.')