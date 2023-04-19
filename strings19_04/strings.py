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


