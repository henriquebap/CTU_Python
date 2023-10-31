from menu import Menu


def main():
    options = [
        ("Create Store","Option 1 : "),
        ("Create Item", "Option 2 :"),
        ("View Stores", "Option 3:"),
        ("Exit", "Option 4 : Exit")
    ]
    main_menu = Menu("Menu Principal",options)
    while True:
        main_menu.show()
        choice = main_menu.get_choice()

        if choice == 4:
            print("EXITING THE PROGRAM. Bye Bye See u later!!")
            break
        elif choice == 1:
            main_menu.create_store()
        elif choice == 2:
            main_menu.create_item()
        elif choice == 3:
            main_menu.get_stores()

if __name__ == "__main__":
    main()