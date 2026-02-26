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

    print(x/y)

else:

    print('Operação inválida e/ou indisponível.')