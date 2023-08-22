import csv
from Tools.get_file import get_file
from Tools.Avarege import org_rate_search, avarege_comparing
from Tools.Options import option, option_budget, option_gross, option_rate, option_main
from Tools.budget import budget_search, calculate_budget_difference, budget_calculator_without_avengers
from Tools.gross import gross_search, gross_search_w_avengers
from Tools.rate import treshold, title_rate_search, organizing, filter_title_rate


def main():
    while True:
        Option_main = option_main()
        if Option_main == 1:
            file_path = input("Digite o caminho do arquivo CSV: ")
            file_content = get_file(file_path)
            if file_content:
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
                                try:
                                    filter_grade = float(input("Coloque uma nota para filtrar os filmes: "))
                                    filter_grade = treshold(filter_grade)
                                    if filter_grade > 10:
                                        print("Porfavor Digite um numero entre 0 e 10")
                                        continue
                                    else:    
                                        title_rate = title_rate_search(file_content)
                                        organizing(title_rate)
                                        
                                        filtered_titles_and_ratings = filter_title_rate(filter_grade, title_rate)

                                        print("---"*3)
                                        print(f"O(s) Filme(s) com a média igual ou maior de {filter_grade}, em Ordem do Melhor para o Pior:")
                                        print("---"*3)
                                        for title_rating in filtered_titles_and_ratings:
                                            print(f"Titulo: {title_rating['Title']}, Nota: {title_rating['Rating']}")
                                except ValueError:
                                    print("Informe um numero valido")
                            elif Option_rate == 0:
                                break
                            else:
                                print("Digite uma opcao valida!")
                    elif Option == 0:
                        break
                    else:
                        print("Porfavor Digite uma opcao valida!")
        elif Option_main == 0:
            print("Saindo do Programa")
            break
        else:
            print("Opcao Invalida")

    

if __name__ == "__main__":
    main()
    