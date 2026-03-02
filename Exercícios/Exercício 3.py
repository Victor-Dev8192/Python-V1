import math as m

x = int(input('Primeiro valor? '))

y = int(input('Segundo valor? '))

Operation = input('Qual operação? (+,-,*,/, ^, √, !, ?, Nome encurtado da operação.) ')

if (Operation == '+' or 'Add'):

    print(x+y)

elif (Operation == '-' or 'Minus'):

    print(x-y)

elif (Operation == '*' or 'Multi'):

    print(x*y)

elif (Operation == '/' or 'Diviz'):

    if y != 0:

        print(x/y)

    else:

        print('Erro Desconhecido: Divisão por zero é impossível.')

if (Operation == '^' or 'Power'):

    print(x.m.power(y))

elif (Operation == '√' or 'Root'):

    print(x.m.sqrt(y))

elif (Operation == '!' or 'Factorial'):

    print(x.m.factorial)

elif (Operation == '?' or 'Termial'):

    print(x*(x+1)/2)

else:

  print('Operação inválida e/ou indisponível.')