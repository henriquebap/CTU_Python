import csv
from tools import get_file, title_rate_search, organizing, treshold, filter_title_rate, org_rate_search
from tools import avarege_comparing

def main():
    file_path = "H:\\User\\Desktop\\rqiue2.0\\Fiap\\CT_Python_Class\\CTU_Python\\PS2\\Checkpoint4\\db.csv"
    file_content = get_file(file_path)
    if not file_content: 
        return

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
        
    print("---"*3)

    org_avg_ratings = org_rate_search(file_content)

    print("Average Ratings by Company:")
    for org, avg_rating in org_avg_ratings.items():
        print(f"Company: {org}, Average Rating: {avg_rating:.2f}")
    
    avarege_comparing(file_content)

if __name__ == "__main__":
    main()