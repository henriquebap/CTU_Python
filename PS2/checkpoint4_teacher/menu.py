import utils
from analytics import Controller


class Menu:
    def compare_ratings(self):
        result = self.controller.compare_ratings()
        
        marvel_gross = result['marvel_score']
        dc_gross = result['dc_score']
        print(f'Segundo o público, a média de avialiação da Marvel é {marvel_gross:.2f}')
        print(f'Segundo o público, a média de avialiação da DC é {dc_gross:.2f}')
        print(result['message'])


    def compare_budget(self):
        result = self.controller.compare_budgets()
        marvel_gross = result['marvel_score']
        dc_gross = result['dc_score']
        print(f'O orçamento da Marvel foi {marvel_gross:,.2f}')
        print(f'O orçamento total da DC foi {dc_gross:,.2f}')
        print(result['message'])

    def compare_gross(self):
        result = self.controller.compare_gross()
        marvel_gross = result['marvel_score']
        dc_gross = result['dc_score']
        print(f'O faturamento da Marvel foi {marvel_gross:,.2f}')
        print(f'O faturamento total da DC foi {dc_gross:,.2f}')
        print(result['message'])

    def filter_movies(self):
        while True:
            rating = input("Digite uma nota para filtrar a listagem de filmes: ")
            rating = utils.get_float(rating)
            if rating:
                break
            print("Informe uma nota válida")

        self.controller.filter_movies(rating)
        
    def __init__(self):
        self.options = [
            {
                "action": self.compare_ratings,
                "description": "Na avaliação do público, quem vence esse duelo?"
            },
            {
                "action": self.compare_budget,
                "description": "Em relação ao orçamento, quem vence esse duelo?"
            },
            {
                "action": self.compare_gross,
                "description": "Em relação ao faturamento, quem vence esse duelo?"
            },
            {
                "action": self.filter_movies,
                "description": "Filtrar filmes por avaliação"
            }
        ]

    def setup_data(self, content):
        self.controller = Controller(content)

    def show_options(self):
        for index, option in enumerate(self.options, 1):
            print(f"{index} - {option['description']}")

        print("Caso queira encerrar o programa, a qualquer momento pressione CTRL + C")

    def handle_input(self):
        while True:
            option = input("Selecione a opção desejada: ")
            option = utils.get_int(option)
            if option:
                break
            print("Informe um número inteiro")
        
        if option > len(self.options):
            print("Selecione uma opção válida")
            print("")
            return

        selected_option = self.options[option - 1]
        action = selected_option['action']
        action()
        input("Pressione enter para continuar...")

