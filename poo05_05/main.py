from classes import Dog, Golden

toto = Dog("Toto", 8)
print(f'Nosso cachorro {toto.species} tem o nome {toto.name} e tem a idade de {toto.age}')
print(toto.details())
print(toto.bark())

print("--" * 10)
Melissa = Golden("Melissa", 1, "Mel")
print(Melissa.details())
print(Melissa.bark())
print(f'O nome do {Golden.species} e {Melissa.name} e tem {Melissa.age} o apelido dela e {Melissa.nickname}')
print(toto.bark())
print(Melissa.bark())

instanciar = isinstance(Melissa, Dog)
if instanciar == True:
    print("Melissa e um cachorro")