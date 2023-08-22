import csv
def get_file(file_path):
    try:
        with open(file_path, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print("Arquivo não encontrado")