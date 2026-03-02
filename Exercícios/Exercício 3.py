import math as m

x = int(input('Primeiro valor? (Se aplica a operações como Fatorial e Termial.) '))

y = int(input('Segundo valor? (Não se aplica a operações como Fatorial e Termial.) '))

Operation = input('Qual operação? (+,-,*,/, ^, √, !, ?, Nome encurtado da operação.) ')

if (Operation == '+' or 'Add'):

    print(x+y)

elif (Operation == '-' or 'Minus'):

    print(x-y)

elif (Operation == '*' or 'Multi'):

    print(x*y)

elif (Operation == '^' or Operation == 'Power'):

    print(m.pow(x,y))

elif (Operation == '√' or Operation == 'Root'):

    print(m.sqrt(x,y))

elif (Operation == '!' or Operation == 'Factorial'):

    print(m.factorial(x))

elif (Operation == '?' or 'Termial'):

    print(x*(x+1)/2)

elif (Operation == '/' or 'Diviz'):

    if y != 0:

        print(x/y)

    else:

        print('Erro Desconhecido: Divisão por zero é impossível.')

else:

  print('Operação inválida e/ou indisponível.')