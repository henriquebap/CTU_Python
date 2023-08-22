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