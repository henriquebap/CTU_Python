from cad_store import store_cad, cad_prod

def option():
    print("1 - Cadastrar uma loja")
    print("0 - Sair")
    Option = int(input())
    return Option

def save_store(store_id, store_name):
    store_disc = {
        'store_id': store_id,
        'store_name': store_name
    }
    stores.append(store_disc)
    return store_disc

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
    elif Option == 0:
        break
    else:
        print("Digite uma opcao valida")

