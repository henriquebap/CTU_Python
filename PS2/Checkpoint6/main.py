from menu import Menu


def main():
    options = [
        ("Create Store","Option 1 : "),
        ("Create Item", "Option 2 :"),
        ("View Stores", "Option 3:"),
        ("Delete Store", "Option 4:"),
        ("Delete Item", "Option 5"),
        ("Exit", "Option 6: Exit")
    ]
    main_menu = Menu("Menu Principal",options)
    while True:
        main_menu.show()
        choice = main_menu.get_choice()

        if choice == 6:
            print("EXITING THE PROGRAM. Bye Bye See u later!!")
            break
        elif choice == 1:
            main_menu.create_store()
        elif choice == 2:
            main_menu.create_item()
        elif choice == 3:
            main_menu.get_stores()
        elif choice == 4:
            main_menu.delete_store()
        elif choice == 5:
            main_menu.delete_item()

if __name__ == "__main__":
    main()