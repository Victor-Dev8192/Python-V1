def Name_Verify ():
    return "Sim!" if 'silva' in Name.lower() else "Não!"

while True: 
 Name = input(str('Qual é o seu nome completo? ')).strip()
 print(f'Seu nome tem silva? {Name_Verify()}')