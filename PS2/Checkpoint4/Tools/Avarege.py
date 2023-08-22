
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
