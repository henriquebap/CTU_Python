import csv
file_path = "D:/CTU_Python/exercicioCSV/animation_series.csv"
with open(file_path, encoding='utf-8') as file: 
    reader = csv.DictReader(file)

    title_ratings = []

    for row in reader:
        rating = float (row["Rating"])
        #rating_values.append(float(rating))
        title = row["Title"]
        title_ratings.append({"Title": title, "Rating": rating})

title_ratings.sort(key=lambda x: x["Rating"], reverse=True)

threshold = 9.0

filtered_titles_and_ratings = [   
   {"Title": title_rating["Title"], "Rating": title_rating["Rating"]}
    for title_rating in title_ratings
    if title_rating["Rating"] >= threshold
]

#print(f"Rating Melhores que {threshold}")

print("Ordenado Rating (Do melhor Para o menor): ")
for title_rating in filtered_titles_and_ratings:
    print(f"Title: {title_rating['Title']}, Rating: {title_rating['Rating']}")

