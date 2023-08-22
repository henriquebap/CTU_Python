
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

