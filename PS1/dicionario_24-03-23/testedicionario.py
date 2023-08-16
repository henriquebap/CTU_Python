import re
def display_user_data(user):
    print("Primeiro nome: " + user['first_name'])
    print("Último Nome: " + user['last_name'])
    print("Idade: " + str(user['age']))
    print()


def create_user(users):
    first_name = input("Qual seu primeiro nome: ")
    first_name = first_name.lower()
    first_name = re.sub(r'[^a-z]','',first_name)
    last_name = input("Qual seu último nome: ")
    last_name = last_name.lower()
    last_name = re.sub(r'[^a-z]','',last_name)
    age = int(input("Qual sua idade: "))
    user_data = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
    }
    users.append(user_data)


def search_user(users):
    first_name = input("Qual usuário deseja visualizar os dados: ")
    #first_name = first_name.lower
    #first_name = re.sub(r'[^a-z]','',first_name)
    for user in users:
        if user['first_name'] == first_name:
            display_user_data(user)
            return

    print("Usuário não encontrado")
    print()

def show_users(users):
    for user in users:
        display_user_data(user)

users = []
while True:
    print("Selecione a opção desejada")
    print("1 - Cadastrar usuário")
    print("2 - Localizar usuário pelo primeiro nome")
    print("3 - Ver todos os usuários")
    print("0 - Sair")
    option = int(input())
    if option == 0:
        break
    
    if option == 1:
        create_user(users)
    elif option == 2:
        search_user(users)
    elif option == 3:
        show_users(users)
