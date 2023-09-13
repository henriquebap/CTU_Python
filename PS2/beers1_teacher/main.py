from utils import columns_to_dict, get_file_content, get_headers, parse_float


def main():
    file_path = input("Informe no seu computador a localização do arquivo: ")
    file_content = get_file_content(file_path)
    if not file_content:
        return
    
    filter_abv = input("Digite o ABV: ")
    filter_abv = parse_float(filter_abv)

    if not filter_abv:
        return    

    headers = get_headers(file_content[0])
    for line in file_content[1:]:
        columns = line.split(",")
        data = columns_to_dict(headers, columns)
        try:
            abv = round(float(data['abv']) * 100, 2)
        except ValueError:
            abv = 0
        
        if abv <= filter_abv:
            print(f"{data['beer']} - ABV: {abv}")

main()
