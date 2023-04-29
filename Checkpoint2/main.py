from cad_store import store_cad, cad_prod

def option():
    print("1 - Cadastrar uma loja")
    print("2 - Cadastrar o Produto")
    print("0 - Sair")
    Option = int(input())
    return Option

def save_store(store_id, store_name):
    store_disc = {
        'store_id': store_id,
        'store_name': store_name,
        'products':[]
    }
    stores.append(store_disc)
    return store_disc

def save_product(store_id, prod_id, prod_nm, prod_desc, prod_price):
    for store in stores:
        if store['store_id'] == store_id:
            prod_disc = {
                'prod_id': prod_id,
                'prod_nm': prod_nm,
                'prod_desc': prod_desc,
                'prod_price': prod_price
            }
            store['products'].append(prod_disc) #adicionar o produto do discionario na lista que contem a loja
            return True
    return False
stores = []
while True:
    Option = option()
    if Option == 1:
       store = store_cad()
       if store:
           save_store(store['store_id'], store['store_name'])
           print("Loja cadastrada com sucesso")
           print(stores)
       else:
           print("Erro: dados de loja invalidos")
    elif Option == 2:
        prod = cad_prod()
        store_id = input("Digite o ID da loja: ")
        if save_product(store_id,prod['prod_id'], prod['prod_nm'], prod['prod_desc'], prod['prod_price']):
            print("Produto cadastrado com sucesso")
            print(stores)
        else:
            print("Loja nao encontrada")
    elif Option == 3:
        for store in stores:
            print("Loja:", store['store_name'])
            if len(store['products']) == 0:
                print("Nenhum produto cadastrado.")
            else:
                for product in store['products']:
                    print("Produto:", product['prod_nm'])
                    print("Descricao:", product['prod_desc'])
                    print("Preco:", product['prod_price'])
    elif Option == 0:
        break
    else:
        print("Digite uma opcao valida")

