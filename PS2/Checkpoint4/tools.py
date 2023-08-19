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
    
    return highest_budget_company, highest_budget