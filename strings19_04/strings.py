#intercao com String boolean
empty=''
if empty:
    print("Tem algo na String")
else:
    print("Esta vazia")

#multiplicação de string
music = 'Na'
print(music * 10, "Batmaaan")


#validação
message = "uma mensagem"
term = "me"
if term in message:
    print("A mensagem", message, "Tem o termo", term)
else:
    print("A mensagem", message, "nao tem o termo", term)

#for into a String
text = 'The quick brown fox jumps over the lazy dog'
#for char in text:
 #   for char in text:
  #      print(char)

# fatiamento de String
print(text[0])#select the char
print("-" * 10)
print(text[4:])#a partir de
print("-" * 10)
print(text[5:11])#escolhe os dois(Start point to end point)
print("-" * 10)
print(text[:5])#Start poit to the 4
print("-" * 10)
print(text[1:10:2])#mostra tudo a partir do segundo caractere ate o decimo caractere
#fatiamento negativo
print("-" * 10)
print(text[0:-2])
print("-" * 10)
#inverter String
print(text[::-1])
print("-" * 10)

#interpolacao de String
name = 'henrique'
number = 123
print(f'hello {name} Seu numero e {number}')
print("-" * 10)

#Methods
#capitalize deixa somente a primeira letra maiuscula
henrique = "henrique"
print(henrique)
print("- antes do capitalize")
henrique = henrique.capitalize()
print(henrique + " depois da capialize + salvando na string")
print("-" * 10)
print(henrique.capitalize())
print("- Colocando captalize mas nao salva na variavel")
print("-" * 10)
print(henrique.center(30)) #centralizando,
print("-" * 10)
print(henrique.count('e'))
print("-" * 10)
print(text.count('a'))
print("-" * 10)
#Strings StartsWith
print(message.startswith('uma'))

print("___" *10)
#retorna em boolean
version = '95'
print(version.startswith('9'))
print("_-_-_-_" *10)
frase = "Meu nome é Henrique"
print(frase.endswith("que"))
print("_-_-_-_" *10)
print(frase.endswith("henr"))
print("_-_-_-_" *10)
print(frase.find("que"))
#index
print("_-_-_-_" *10 + "index")
print(frase.index("Henrique"))
#islnum
#retorna alfanumerico
print("_-_-_-_" *10 + "islnum")
message2 = "mensagem \u0002"
print(message2.isalnum())
print(message2.isalpha())
#isdigit
print("_-_-_-_" *10 + "isdigit")
text = '123456'
print(text.isdigit())
notdigit = "Ola"
print(notdigit.isdigit())
is_float = "2.5"
print(is_float.isdigit())
#isnumeric
print("_-_-_-_" *10 + "isNumeric")
print(text, text.isnumeric())
#space
print("_-_-_-_" *10 + "isSpace")
space = "  "
print(space.isspace())
#lower :) & islower
print("_-_-_-_" *10 + "lower")
to_lower = "AAAAAAAAAA TO DOIDO"
print(to_lower.lower())
to_lower = to_lower.lower()
print(to_lower)
print(to_lower.islower())
#name = input("Digite o nome: ").lower()
print(name)
#Upper ;( para gritar
print("_-_-_-_" *10 + "Upper")
name = name.upper()
print(name)
#title 
print("_-_-_-_" *10 + "Title")
print(name.title())
#join so funciona com Strings
print("_-_-_-_" *10 + "Join")
words = ["Henrique", "Oliveira", "Baptista"]
print(words)
print(" ".join(words))
#Strip - limpar os caracteres da String :o
print("_-_-_-_" *10 + "Strip")
filme = "           Velozes e furiosos  "
print(filme.strip())
filme2 = "$$#%@!¨#&#*( The Recruit     ##"
print(filme2.strip("$$#%@!¨#&#* ("))
#ltrip limpa para a esquerda
print(filme2.lstrip("$$#%@!¨#&#* ("))
#rStrip para a direita
print(filme2.rstrip("$$#%@!¨#&#* ("))
#Replace subsititui
print("_-_-_-_" *10 + "REPLACE")
love = "Eu amo pipoca, affs tchau. tchau pipoca"
print(love.replace("pipoca", "nutella"))
#split
print("_-_-_-_" *10 + "SPLIT")
new_list = "Eu prefiro nescal do que toddy".split()
print(new_list)
print("_-_-_-_" *10 + "Strip")



