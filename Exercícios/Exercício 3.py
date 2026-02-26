x = int(input('Primeiro valor? '))

y = int(input('Segundo valor? '))

Operation = input('Qual operação? (+,-,*,/) ')

if (Operation == '+'):

    print(x+y)

elif (Operation == '-'):

    print(x-y)

elif (Operation == '*'):

    print(x*y)

elif (Operation == '/'):

    if y != 0:

        print(x/y)

    else:

        print('Erro Desconhecido: Divisão por zero é impossível.')

else:

  print('Operação inválida e/ou indisponível.')