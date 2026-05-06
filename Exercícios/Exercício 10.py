def Name_Verify (Name):
    return "Sim!" if 'silva' in Name.lower() else "Não!"

while True: 
 Name = input(str('\nQual é o seu nome completo? ')).strip()
 print(f'\nSeu nome tem silva? {Name_Verify(Name)}')