
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
