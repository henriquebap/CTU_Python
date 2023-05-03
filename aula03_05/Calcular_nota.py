import requests

name = input("Digite o seu nome: ").strip()
response = requests.get(
    f'http://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}'
)
print(response.json())




def calcular_nota(nota):
    total = nota / 2
    return total
nota = int(input("Digite a sua nota: "))
print(f'Sua nota final é {nota}')



for x in range(10):
    if x % 2 == 0:
        print("Numero", x)


users = []
while True:
    first_name = input("Digite Seu primeiro nome: ")
    last_name = input("Digite o seu sobrenome: ")
    email = input("Digite o seu email: ")
    user_data = {
        'first_name': first_name.strip(),
        'last_name': last_name.strip(),
        'email': email.lower().strip()
    }
    print("Dados do usuario", user_data)
    users.append(user_data)
