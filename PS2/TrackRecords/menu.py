from database import crud


class Menu:
    def json_path(self):
        json_file_path = input("Passe o Arquivo Json aqui: ")

        return json_file_path
    
    def new_track(self, json_file_path):
        crud.create_track(json_file_path)