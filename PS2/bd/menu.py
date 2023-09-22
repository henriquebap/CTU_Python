import utils
from database import crud


class Menu:
    def create_user(self):
        first_name = input("Digite o primeiro nome: ")
        last_name = input("Digite o sobrenome: ")
        email = input("Digite o email: ")

        user = crud.create_user(first_name, last_name, email)
        print(f"Usuário criado com sucesso! Id -> {user.id}")

    def show_users(self):
        users = crud.get_users()
        for user in users:
            print()
            print(f"id -> {user.id}")
            print(f"Nome -> {user.get_fullname()}")
            print(f"Email -> {user.email}")

    def create_item(self):
        while True:
            owner_id = input("Informe o ID do usuário: ")
            owner_id = utils.get_int(owner_id)
            if not owner_id:
                print("Digite um número inteiro")
                continue

            owner = crud.get_user(owner_id)
            if not owner:
                print("Usuário não encontrado. Informe um dos IDs informados na lista a seguir")
                self.show_users()
                continue
            break

        title = input("Digite o título do item: ")
        description = input("Digite sua descrição: ")

        item = crud.create_item(title, description, owner)
        print(f"Item criado com sucesso! Id -> {item.id}")

    def show_items(self):
        items = crud.get_items()
        for item in items:
            print()
            print(f"id -> {item.id}")
            print(f"Título -> {item.title}")
            print(f"Descrição -> {item.description}")
            print(f"Usuário -> {item.owner_id}")

    def delete_user(self):
        while True:
            user_id = input("Informe o ID do usuário: ")
            user_id = utils.get_int(user_id)
            if user_id:
                break
            print("Digite um número inteiro")
        
        crud.delete_user(user_id)
        print(f"Usuário {user_id} deletado com sucesso!")
        
    def __init__(self):
        self.options = [
            {
                "action": self.create_user,
                "description": "Criar usuário"
            },
            {
                "action": self.show_users,
                "description": "Mostrar usuários"
            },
            {
                "action": self.delete_user,
                "description": "Deletar usuário"
            },
            {
                "action": self.create_item,
                "description": "Criar item"
            },
            {
                "action": self.show_items,
                "description": "Mostrar itens"
            },
        ]

    def show_options(self):
        for index, option in enumerate(self.options, 1):
            print(f"{index} - {option['description']}")

        print("Caso queira encerrar o programa, a qualquer momento pressione CTRL + C")

    def handle_input(self):
        while True:
            option = input("Selecione a opção desejada: ")
            option = utils.get_int(option)
            if option:
                break
            print("Informe um número inteiro")
        
        if option > len(self.options):
            print("Selecione uma opção válida")
            print("")
            return

        selected_option = self.options[option - 1]
        action = selected_option['action']
        action()
        input("Pressione enter para continuar...")

