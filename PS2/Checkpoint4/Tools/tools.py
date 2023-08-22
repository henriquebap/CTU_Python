import csv
def get_file(file_path):
    try:
        with open(file_path, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print("Arquivo não encontrado")

def title_rate_search(reader):
    title_rate = []
    for row in reader:
        rating = float (row ["Rate"])
        title = row["Original Title"]
        title_rate.append({"Title": title, "Rating": rating}) 
    return title_rate

def organizing(title_rate):
    title_rate.sort(key=lambda x: x["Rating"], reverse=True)

def treshold(grade):
    try:
        result = float(grade)
        return result
    except ValueError:
        print("Informe um numero valido")

def filter_title_rate(result, title_rate):
    filtered_titles_and_ratings = [   
        {"Title": title_rating["Title"], "Rating": title_rating["Rating"]}
            for title_rating in title_rate
            if title_rating["Rating"] >= result
]
    
    if not filtered_titles_and_ratings:
        print("Nao Existe nenhum filme com essa nota.")

    return filtered_titles_and_ratings

def org_rate_search(reader):
    org_ratings = {}  # Dictionary to store ratings for each company
    org_counts = {}   # Dictionary to store counts of entries for each company
    
    for row in reader:
        rating = float(row["Rate"])
        org = row["Company"]
        
        # Update the company's rating and count
        if org in org_ratings:
            org_ratings[org] += rating
            org_counts[org] += 1
        else:
            org_ratings[org] = rating
            org_counts[org] = 1
    
    # Calculate average rating for each company
    org_avg_ratings = {
        org: org_ratings[org] / org_counts[org]
        for org in org_ratings
    }
    
    return org_avg_ratings

def avarege_comparing(file_content):
    org_avg_rating = org_rate_search(file_content)

    marvel_avg = org_avg_rating.get("Marvel", 0.0)
    dc_avg = org_avg_rating.get("DC", 0.0)

    if marvel_avg > dc_avg:
        print("A empresa Marvel tem a maior medias de notas")
    elif dc_avg > marvel_avg:
        print("A empresa Dc tem a maior media de notas.")
    else:
        print("Marvel e Dc tem as mesmas notas de media.")

def budget_search(reader):
    bud_totals = {}
    
    for row in reader:
        budget = float(row["Budget"])
        org = row["Company"]

       # Update the company's total budget
        if org in bud_totals:
            bud_totals[org] += budget
        else:
            bud_totals[org] = budget
    
    # Find the company with the highest total budget
    highest_budget_company = max(bud_totals, key=bud_totals.get)
    highest_budget = bud_totals[highest_budget_company]
    
    lowest_budget_company = min(bud_totals, key=bud_totals.get)
    lowest_budget = bud_totals[lowest_budget_company]
    
    return highest_budget_company, highest_budget, lowest_budget_company, lowest_budget


def budget_calculator_without_avengers(reader):
    bud_totals = {}
    
    for row in reader:
        budget = float(row["Budget"])
        org = row["Company"]
        title = row["Original Title"]

        # Exclude movies with "Avengers" in the title
        if "Avengers" not in title:
            # Update the company's total budget
            if org in bud_totals:
                bud_totals[org] += budget
            else:
                bud_totals[org] = budget
    
    # Find the company with the highest total budget
    highest_budget_company = max(bud_totals, key=bud_totals.get)
    highest_budget = bud_totals[highest_budget_company]
    
    lowest_budget_company = min(bud_totals, key=bud_totals.get)
    lowest_budget = bud_totals[lowest_budget_company]
    
    return highest_budget_company, highest_budget, lowest_budget_company, lowest_budget

def calculate_budget_difference(highest_budget, lowest_budget):
    difference = highest_budget - lowest_budget
    return difference


def gross_search(reader):

    gross_totals = {}
    
    for row in reader:
        gross_earnings = float(row["Gross Worldwide"])
        org = row["Company"]

        # Update the company's total gross earnings
        if org in gross_totals:
            gross_totals[org] += gross_earnings
        else:
            gross_totals[org] = gross_earnings
    
    return gross_totals


def gross_search_w_avengers (reader):

    gross_totals = {}
    
    for row in reader:
        gross_earnings = float(row["Gross Worldwide"])
        org = row["Company"]
        title = row["Original Title"]

        if "Avengers" not in title:
            if org in gross_totals:
                gross_totals[org] += gross_earnings
            else:
                gross_totals[org] = gross_earnings
        
    return gross_totals

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