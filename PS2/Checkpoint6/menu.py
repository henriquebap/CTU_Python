from database import crud
import utils

class Menu:
    def __init__(self, title, options):
        self.title = title
        self.options = options

    def show(self):
        print(self.title)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option[0]}")
    
    def get_choice(self):
        try:
            choice = int(input("Enter your choice (number): "))
            if 1 <= choice <= len(self.options):
                return choice
            else:
               print("Invalid Option!, Try Again")
               return self.get_choice()
        except ValueError:
            print("Invalid Option, Try another option!")
            return self.get_choice()
        
    def create_store(self):
        name = input('Please enter the name of the new store: ')

        store = crud.create_store(name)
        print(f"Store Successfully Created {store.id}")
            
    def create_item(self):
        store_id = self.store_id_validation()

        name = input('Please enter the name of the new item: ')
        description = input('Write a description: ')
        price = float(input('Set a price: '))
        item = crud.create_item(name, description, price, store_id)
        print(f"Item '{item.name}' created and associated with store '{store_id}'.")
        
    def get_stores(self):
        stores = crud.get_stores_with_items()
        for store in stores:
            print("--"*5)
            print(f"Store ID -- {store.id}")
            print(f"Store Name -- {store.name}")
            print("Itens:")
            for item in store.itens:
                print(f"  Item ID -- {item.id}")
                print(f"  Item Name -- {item.name}")
                print(f"  Item Description -- {item.description}")
                print(f"  Item Price -- {item.price}")
                print("--"*5)

    def delete_store(self):
        store_id = self.store_id_validation()
        if store_id is not None:
            store = crud.get_store_by_id(store_id)
            if store is not None:
                confirmation = str(input(f"Are you sure about deleting the store '{store.name}' with ID {store_id}? (y/n)"))
                if confirmation.lower() == "y":
                    if crud.delete_store_by_id(store_id):
                        print(f"Store '{store.name}' with ID {store_id} deleted.")
                    else:
                        print(f"Failed to delete store '{store.name}' with ID {store_id}.")
                else:
                    print("Operation canceled")
            else:
                print(f"Store with ID {store_id} not found.")


    def delete_item(self):
        print("De qual loja o item voce quer excluir?")
        store_id = self.store_id_validation()

        if store_id is not None:
            items = crud.get_items_from_store(store_id)

            if not items:
                print("There is no Itens in this Store.")
                return

            
            while True:
                try:
                    print("\nItens disponíveis para exclusão:")
                    for i, item in enumerate(items, start=1):
                        print(f"{i}) Store ID - {item.store_id}, Item ID - {item.id}, Nome do item - {item.name}")
                    index = int(input("\nDigite o índice do item que deseja deletar (0 para sair): "))

                    if index == 0:
                        return  # Sair do método se o usuário digitar 0
                    elif 1 <= index <= len(items):
                        item_to_delete = items[index - 1]
                        
                        print(f"Deseja realmente deletar o item '{item_to_delete.name}' com preço de R${item_to_delete.price}? (Y/N): ")
                        confirmation = input().strip().lower()

                        if confirmation == "y":
                            if crud.delete_item_by_id(item.id):
                                print(f"Item '{item.name}' deleted from store '{store_id}'.")
                            else:
                                print(f"Failed to delete item '{item.name}' from store '{store_id}'.")
                            break
                        elif confirmation == "n":
                            print("Operation Canceled!")
                            break
                        else:
                            print("Please 'Y' to confirm and 'N' to not confirm")
                    else:
                        print("Index out of len, Try Again! ")
                except ValueError:
                    print("Digite um valor numérico válido ou 0 para sair.") 
                    
                
                      







    def store_id_validation(self):
        while True:
            try:
                store_id = int(input('Enter the store ID: '))
                validated_store = crud.get_store_by_id(store_id)
                if validated_store is not None:
                    return store_id
                else:
                    print("Store not found, valid IDs are: ")
                    self.get_stores()
            except ValueError:
                print('Invalid Store ID, please enter a valid integer.')