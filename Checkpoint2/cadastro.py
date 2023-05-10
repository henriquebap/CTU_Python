import re
def store_cad():
    validar_numero = r"^\d+$" #"regex"  faz a verificação da entrada se corresponde a expressao regular(re.match)
    while True:
        store_id = input("Digite o id da loja: ")
        if re.match(validar_numero, store_id):
        # Converter a string em um número inteiro
            store_nm = int(store_id)
            break
        else:
            print("Porfavor digie um ID valido, usando numeros")
            continue
    while True:
        store_name = input("Digite o nome da loja: ").lower()
        if store_name.isalpha():
            store_name = re.sub(r'[^a-z]','',store_name).strip("$$#%@!¨#&#* (")
            break
        else:
            print("Porfavor digite somente numeros no nome da loja")
            continue
    store_disc = {
        'store_id': store_id,
        'store_name': store_name
    }
    if store_id and store_name:  # add a check to make sure store_id and store_name are not None
        return store_disc
    else:
        return None
    
def cad_prod():
    validar_numero = r"^\d+$"
    while True:
        prod_id = input("Digite o id do produto: ")
        if re.match(validar_numero, prod_id):
            prod_nmb = int(prod_id)
            break
        else:
            print("Porfavor digie um ID valido, usando numeros")
            continue
    while True:
        prod_nm = input("Digite o nome do produto: ").lower()
        if prod_nm.isalpha():
            prod_nm = re.sub(r'[^a-z]','',prod_nm).strip("#$$%@!¨#&#* (")
            break
        else:
            print("Digite o nome usando apenas letras")
            continue
    prod_desc = input("Coloque uma descricao para o produto: ")
    while len(prod_desc) > 50:
        print("A descricao do produto deve ter no máximo 50 caracteres.")
        prod_desc = input("Coloque uma descricao para o produto: ")
    while True:
        prod_price = input("Valor do produto: ")
        if prod_price.isdigit():
            prod_price = float(prod_price)
            break
        else:
            print("Porfavor digite somente numeros")
            continue
    prod_disc = {
                'prod_id': prod_id,
                'prod_nm': prod_nm,
                'prod_desc': prod_desc,
                'prod_price': prod_price
            }
    if prod_id and prod_nm and prod_price:
        return prod_disc
    else:
        return None