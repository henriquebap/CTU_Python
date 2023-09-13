class Controller:
    def __init__(self, content):
        self.marvel_analytics = Analytics()
        self.dc_analytics = Analytics()
        self.get_headers(content[0])
        self.get_data(content[1:])

    def to_dict(self, columns):
        data = {}
        for index, column in enumerate(self.headers):
            column_data = columns[index]
            data[column] = column_data.strip().strip('"')
        return data

    def get_headers(self, line):
        self.headers = []
        for header in line.split(","):
            self.headers.append(header.strip().strip('"'))  

    def get_data(self, lines):
        for line in lines:
            columns = line.split(",")
            data = self.to_dict(columns)
            if data["Company"] == 'DC':
                self.dc_analytics.add_movie(data)
            elif data["Company"] == "Marvel":
                self.marvel_analytics.add_movie(data)

    def compare_ratings(self):
        marvel_average_rating = self.marvel_analytics.calculate_average_rating()
        dc_average_rating = self.dc_analytics.calculate_average_rating()

        return self.get_result(marvel_average_rating, dc_average_rating)

    def compare_budgets(self):
        marvel_budget = self.marvel_analytics.calculate_budget()
        dc_budget = self.dc_analytics.calculate_budget()

        return self.get_result(marvel_budget, dc_budget)
        
    def compare_gross(self):
        marvel_gross = self.marvel_analytics.calculate_gross()
        dc_gross = self.dc_analytics.calculate_gross()

        return self.get_result(marvel_gross, dc_gross)

    def get_result(self, marvel_score, dc_score):
        message = ''
        if marvel_score > dc_score:
            message = "Neste duelo, a Marvel vence"
        elif marvel_score > dc_score:
            message = "Neste duelo, a DC vence"
        else:
            message = "Neste duelo, temos um empate"
        
        return {
            'message': message,
            'marvel_score': marvel_score,
            'dc_score': dc_score
        }

    def filter_movies(self, rating):
        all_movies = self.dc_analytics.movies + self.marvel_analytics.movies
        for movie in all_movies:
            movie_rating = float(movie["Rate"])
            if movie_rating >= rating:
                print(f"Filme: {movie['Original Title']} -> Avaliação: {movie_rating}")

class Analytics:
    def __init__(self):
        self.movies = []
        self.average_rating = None
        self.total_budget = None
        self.total_gross = None
    
    def add_movie(self, movie_data):
        self.movies.append(movie_data)

    def calculate_gross(self):
        if self.total_gross:
            return self.total_gross
        
        self.total_gross = self.get_total("Gross Worldwide")
        return self.total_gross

    def calculate_budget(self):
        if self.total_budget:
            return self.total_budget
        
        self.total_budget = self.get_total("Budget")        
        return self.total_budget

    def calculate_average_rating(self):
        if self.average_rating:
            return self.average_rating
        
        self.average_rating = self.get_total("Rate")
        
        self.average_rating = self.average_rating / len(self.movies)
        return self.average_rating
    
    def get_total(self, column):
        total = 0
        for movie in self.movies:
            total += float(movie[column])
        return total
