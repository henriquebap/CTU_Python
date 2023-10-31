from database import crud

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
        store_id = int(input('Enter the store ID for this item: '))
        store = crud.get_store_by_id(store_id)
        if store is not None:
            name = input('Please enter the name of the new item: ')
            description = input('Write a description: ')
            price = float(input('Set a price: '))
            item = crud.create_item(name, description, price, store)
            print(f"Item '{item.name}' created and associated with store '{store.name}'.")
        else:
            print("That Store does not exist.")

    def get_stores(self):
        stores = crud.get_stores_with_items()
        for store in stores:
            print()
            print(f"id -- {store.id}")
            print(f"Name -- {store.name}")
            print("Itens:")
            for item in store.itens:
                print(f"  Item ID -- {item.id}")
                print(f"  Item Name -- {item.name}")
                print(f"  Item Description -- {item.description}")
                print(f"  Item Price -- {item.price}")