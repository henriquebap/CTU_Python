from cadastro import store_cad, cad_prod
# Henrique Oliveira Baptista RM: 97796
def option():
    print("----" * 10)
    print("1 - Cadastrar uma loja")
    print("2 - Cadastrar o Produto")
    print("3 - Mostrar Produtos cadastrados")
    print("0 - Sair")
    print("----" * 10)

    while True:
        Option = input()
        if Option.isdigit():
            Option = int(Option)
            return Option
        else:
            print("Digite uma opcao valida")
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
            print("Loja cadastrada com sucesso\n")
        else:
            print("Erro: dados de loja invalidos")
    elif Option == 2:
        if len (stores) == 0:
             print("Nenhuma Loja Cdastrada")
        else:
            store_id = input("Digite o ID da loja: ")
            if store_id == store['store_id']:
                prod = cad_prod()
                if save_product(store_id,prod['prod_id'], prod['prod_nm'], prod['prod_desc'], prod['prod_price']):
                    print("Produto cadastrado com sucesso\n")
                else:
                    print("Produto nao cadastrado")
            else:
                print("Loja nao encontrada")
    elif Option == 3:
        for store in stores:
            print("---- Loja --------")
            print("Loja:", store['store_name'])
            print("----" * 4)
            if len(store['products']) == 0:
                print("Nenhum produto cadastrado.")
            else:
                for product in store['products']:
                    print("Produto:", product['prod_nm'])
                    print("Descricao:", product['prod_desc'])
                    print("Preco:", product['prod_price'],"\n")
    elif Option == 0:
        break
    