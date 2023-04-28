import re
def store_cad():
    validar_numero = r"^\d+$" #"regex"  faz a verificação da entrada se corresponde a expressao regular(re.match)
    store_id = input("Digite o id da loja: ")
    if re.match(validar_numero, store_id):
    # Converter a string em um número inteiro
        store_nmb = int(store_id)
        print("O número digitado foi:", store_nmb)
    else:
        print("Porfavor digie um ID valido, usando numeros")
    store_name = input("Digite o nome da empresa: ").lower()
    store_name = re.sub(r'[^a-z]','',store_name).strip("$$#%@!¨#&#* (")
    store_disc = {
        'store_id': store_id,
        'store_name': store_name
    }
    return store_disc
def cad_prod():
    validar_numero = r"^\d+$"
    prod_id = input("Digite o id do produto: ")
    if re.match(validar_numero, prod_id):
        prod_nmb = int(prod_id)
        print("O número digitado foi:", prod_nmb)
    else:
        print("Porfavor digie um ID valido, usando numeros")
        return prod_id
    prod_nm = input("Digite o nome do produto: ").lower()
    prod_nm = re.sub(r'[^a-z]','',prod_nm).strip("$$#%@!¨#&#* (")
    prod_desc = input("Coloque uma descricao para o produto: ")
    while len(prod_desc) > 50:
        print("A descricao do produto deve ter no máximo 50 caracteres.")
        prod_desc = input("Coloque uma descricao para o produto")
    prod_price = input("Valor do produto: ")
    prod_price = float(prod_price)