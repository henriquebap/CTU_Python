import csv
from tools import get_file, title_rate_search, organizing, treshold, filter_title_rate, org_rate_search,option_rate
from tools import avarege_comparing, budget_search, calculate_budget_difference,gross_search, option, budget_calculator_without_avengers,option_budget,option_gross,gross_search_w_avengers

def main():
    file_path = "H:\\User\\Desktop\\rqiue2.0\\Fiap\\CT_Python_Class\\CTU_Python\\PS2\\Checkpoint4\\db.csv"
    file_content = get_file(file_path)
    if not file_content: 
        return


    while True:
        Option = option()
        if Option == 1:
            print("---"*3)

            org_avg_ratings = org_rate_search(file_content)

            print("Média de Notas divido por Empresa:")
            for org, avg_rating in org_avg_ratings.items():
                print(f"Empresa: {org}, Com uma Média de nota de: {avg_rating:.2f}")
    
            avarege_comparing(file_content)

        elif Option == 2:  
                while True:
                    option_bud = option_budget()
                    if option_bud == 1:   
                        highest_budget_company, highest_budget, lowest_budget_company, lowest_budget = budget_search(file_content)
                        print("-----"*10)
                        print(f"A Empresa com o maior orçamento é a  {highest_budget_company} com um orçamento total de ${highest_budget:.2f}")
                        print(f"e a {lowest_budget_company} e a menor empresa com o orçamento de ${lowest_budget:.2f}")
                    elif option_bud == 2:
                        budget_difference = calculate_budget_difference(highest_budget, lowest_budget)
                        print("-----"*10)
                        print(f"A diferença do orçamento entre as empreas é de ${budget_difference:.2f}")
                    elif option_bud == 3:        
                        highest_budget_company, highest_budget, lowest_budget_company, lowest_budget = budget_calculator_without_avengers(file_content)
                        print("-----"*10)
                        print("Tirando Avengers da Lista o resultado fica....")
                        print(f"A Empresa com o maior orçamento mesmo sem avengers é {highest_budget_company} com um orçamento total de ${highest_budget:.2f}")
                        print(f"Infelizmente a {lowest_budget_company} continua sendo a menor empresa com o orçamento de ${lowest_budget:.2f}")
                    elif option_bud == 0:
                        break
                    else:
                        print("Porfavor Digite uma opcao valida")
        elif Option == 3:
            while True:
                    Option_gross = option_gross()
                    if Option_gross == 1:        
                        print("-----"*10)
                        gross_earnings = gross_search(file_content)
                        highest_gross_company = max(gross_earnings, key=gross_earnings.get)
                        highest_gross_earnings = gross_earnings[highest_gross_company]
                        print(f"A Empresa com um maior faturamento pelo mundo todo é {highest_gross_company} Com um total de Ganhos de ${highest_gross_earnings:.2f}")
                    elif Option_gross == 2:
                        print("-----"*10)
                        lowest_gross_company = min(gross_earnings, key=gross_earnings.get)
                        lowest_gross_earnings = gross_earnings[lowest_gross_company]
                        print(f"A empresa {lowest_gross_company} teve um faturamento de ${lowest_gross_earnings}")
                    elif Option_gross == 3:
                        print("-----"*10)
                        lowest_gross_company = min(gross_earnings, key=gross_earnings.get)
                        lowest_gross_earnings = gross_earnings[lowest_gross_company]
                        earnings_difference = highest_gross_earnings - lowest_gross_earnings
                        print(f"A diferença de faturamento entre as duas é de ${earnings_difference:.2f}")
                    elif Option_gross == 4:
                        print("-----"*10)
                        gross_earnings = gross_search_w_avengers(file_content)
                        highest_gross_company = max(gross_earnings, key=gross_earnings.get)
                        highest_gross_earnings = gross_earnings[highest_gross_company]
                        print("*Removendo Avengers*")
                        print(f"A Empresa com um maior faturamento pelo mundo todo é {highest_gross_company} Com um total de Ganhos de ${highest_gross_earnings:.2f}")
                    elif Option_gross == 0:
                        break
                    else:
                        print("Digite uma Opcao Valida!")
        elif Option == 4:
            while True:
                Option_rate = option_rate()
                if Option_rate == 1:
                    filter_grade = input("Coloque uma nota para filtrar os filmes: ")
                    filter_grade = treshold(filter_grade)
                    if filter_grade > 10:
                        print("Porfavor Digite um numero entre 0 e 10")
                    else:
                        continue
                    title_rate = title_rate_search(file_content)
                    organizing(title_rate)
                    
                    filtered_titles_and_ratings = filter_title_rate(filter_grade, title_rate)

                    print("---"*3)
                    print(f"O(s) Filme(s) com a média igual ou maior de {filter_grade}, em Ordem do Melhor para o Pior:")
                    print("---"*3)
                    for title_rating in filtered_titles_and_ratings:
                        print(f"Titulo: {title_rating['Title']}, Nota: {title_rating['Rating']}")
                elif Option_rate == 0:
                    break
                else:
                    print("Digite uma opcao valida!")




'''
    filter_grade = input("Coloque a nota que queira ver: ")
    filter_grade = treshold(filter_grade)

    title_rate = title_rate_search(file_content)
    organizing(title_rate)
    
    filtered_titles_and_ratings = filter_title_rate(filter_grade, title_rate)

    print("---"*3)
    print(f"Titles with Ratings greater than or equal to {filter_grade}, ordered by Rating:")
    print("---"*3)
    for title_rating in filtered_titles_and_ratings:
        print(f"Title: {title_rating['Title']}, Rating: {title_rating['Rating']}")
        
    #print("---"*3)
#
 #   org_avg_ratings = org_rate_search(file_content)
#
 #   print("Average Ratings by Company:")
  #  for org, avg_rating in org_avg_ratings.items():
   #     print(f"Company: {org}, Average Rating: {avg_rating:.2f}")
    
    #avarege_comparing(file_content)

    
    highest_budget_company, highest_budget, lowest_budget_company, lowest_budget = budget_search(file_content)
    print(f"The company with the highest total budget is {highest_budget_company} with a total budget of ${highest_budget:.2f}")
    print(f"e a {lowest_budget_company} e a menor empresa com lucro de ${lowest_budget:.2f}")


    budget_difference = calculate_budget_difference(highest_budget, lowest_budget)

    print(f"The difference between the highest and lowest budgets is ${budget_difference:.2f}")

    gross_earnings = gross_search(file_content)
    highest_gross_company = max(gross_earnings, key=gross_earnings.get)
    highest_gross_earnings = gross_earnings[highest_gross_company]

    print(f"The company with the highest gross worldwide earnings is {highest_gross_company} with a total earnings of ${highest_gross_earnings:.2f}")
    
    lowest_gross_company = min(gross_earnings, key=gross_earnings.get)
    lowest_gross_earnings = gross_earnings[lowest_gross_company]

    earnings_difference = highest_gross_earnings - lowest_gross_earnings
    print(f"The difference between the highest and lowest gross earnings is ${earnings_difference:.2f}")
    
'''

if __name__ == "__main__":
    main()
    