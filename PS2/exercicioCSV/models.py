import csv

# Option 1: Double backslashes
file_path = "H:\\User\\Desktop\\rqiue2.0\\Fiap\\CT_Python_Class\\CTU_Python\\PS2\\exercicioCSV\\animation_series.csv"

# Option 2: Use a raw string literal
# file_path = r"H:\User\Desktop\rqiue2.0\Fiap\CT_Python_Class\CTU_Python\PS1\exercicioCSV\animation_series.csv"

with open(file_path, encoding='utf-8') as file:
    reader = csv.DictReader(file)
    # rest of your code...

    title_ratings = []

    for row in reader:
        rating = float (row["Rating"])
        #rating_values.append(float(rating))
        title = row["Title"]
        title_ratings.append({"Title": title, "Rating": rating})

title_ratings.sort(key=lambda x: x["Rating"], reverse=True)

threshold = 9.8

filtered_titles_and_ratings = [   
   {"Title": title_rating["Title"], "Rating": title_rating["Rating"]}
    for title_rating in title_ratings
    if title_rating["Rating"] >= threshold
    
]

#print(f"Rating Melhores que {threshold}")

print("Ordenado Rating (Do melhor Para o menor): ")
for title_rating in filtered_titles_and_ratings:
    print(f"Title: {title_rating['Title']}, Rating: {title_rating['Rating']}")

