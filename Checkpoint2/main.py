from cad_store import store_cad, cad_prod

def option():
    print("1 - Cadastrar uma loja")
    print("0 - Sair")

    Option = int(input())
    return Option
 
stores = []
while True:
    Option = option()
    if Option == 1:
        store = store_cad()
        print("Loja cadastrada com sucesso")
        stores.append(store)
        if store:
            while True:
                prod = cad_prod()
    elif Option == 0:
        break
    else:
        print("Digite uma opcao valida")