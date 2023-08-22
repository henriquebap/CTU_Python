
def option():
    print("-----"*10)
    print("Ola User!! Qual Opcao do nosso sistema voce gostaria de escolher? (Digite um numero)")
    print("1 - Para abrir a Media de nota da Marvel vs DC")
    print("2 - Para abrir quem tem o maior orçamentos nos filmes")
    print("3 - Para visualizar quem tem o maior faturamento")
    print("4 - Para visualizar a nota dos filmes")
    print("0 - Para sair")
    print("-----"*10)

    while True:
            Option = input()
            if Option.isdigit():
                Option = int(Option)
                return Option
            else:
                print("Digite um numero para selecionar uma opcao")
                return Option
        
def option_budget():
    print("-----"*10)
    print("Selecione a Opcao que deseja visualizar")
    print("1 - Ver as Notas gerais")
    print("2 - Ver a diferença das notas")
    print("3 - Visualizar a media se a marvel nunca tivesse feito o melhor filme deles - Avengers")
    print("0 - Para Voltar")

    while True:
            option_bud = input()
            if option_bud.isdigit():
                option_bud = int(option_bud)
                return option_bud
            else:
                print("Digite um numero para selecionar uma opcao")
                return option_bud
            

def option_gross():
    print("-----"*10)
    print("1 - Ver a empresa com o maior faturamento")
    print("2 - Ver a media da empresa com o menor faturamento")
    print("3 - A diferenca entre as duas empresas")
    print("4 - Ver a diferenca se a Marvel nao tivesse feito Avengers")
    print("0 - Para voltar")

    while True:
            Option_gross = input()
            if Option_gross.isdigit():
                Option_gross = int(Option_gross)
                return Option_gross
            else:
                print("Digite um numero para selecionar uma opcao")
                return Option_gross
            
def option_rate():
    print("-----"*10)
    print("1 - Para definir a nota:")
    print("0 - Para sair")

    while True:
            Option_rate = input()
            if Option_rate.isdigit():
                Option_rate = int(Option_rate)
                return Option_rate
            else:
                print("Digite um numero para selecionar uma opcao")
                return Option_rate
            
def option_main():
    print("_____ Seja Bem Vindo ao MARVEL VS DC System __________")
    print("Cole o caminho do arquivo db.csv aqui profavor")
    print("---"*10)
    
    print("1 - Para colocar o arquivo")
    print("0 - Para sair")
    while True:
            option = input()
            if option.isdigit():
                option = int(option)
                return option
            else:
                print("Digite um numero para selecionar uma opcao")
                return option
                