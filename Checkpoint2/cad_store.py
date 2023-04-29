import re
def store_cad():
    validar_numero = r"^\d+$" #"regex"  faz a verificação da entrada se corresponde a expressao regular(re.match)
    store_id = input("Digite o id da loja: ")
    if re.match(validar_numero, store_id):
    # Converter a string em um número inteiro
        store_nmb = int(store_id)
    else:
        print("Porfavor digie um ID valido, usando numeros")
        return store_id
    store_name = input("Digite o nome da loja: ").lower()
    store_name = re.sub(r'[^a-z]','',store_name).strip("$$#%@!¨#&#* (")
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
    prod_id = input("Digite o id do produto: ")
    if re.match(validar_numero, prod_id):
        prod_nmb = int(prod_id)
    else:
        print("Porfavor digie um ID valido, usando numeros")
        return prod_id
    prod_nm = input("Digite o nome do produto: ").lower()
    prod_nm = re.sub(r'[^a-z]','',prod_nm).strip("$$#%@!¨#&#* (")
    prod_desc = input("Coloque uma descricao para o produto: ")
    while len(prod_desc) > 50:
        print("A descricao do produto deve ter no máximo 50 caracteres.")
        prod_desc = input("Coloque uma descricao para o produto: ")
    prod_price = input("Valor do produto: ")
    prod_price = float(prod_price)
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