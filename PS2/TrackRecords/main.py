from menu import Menu

if __name__ == "__main__":
    menu = Menu()
    json_file_path = menu.json_path()
    menu.new_track(json_file_path)