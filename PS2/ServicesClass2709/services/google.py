import requests

def get_books(name):
    url = '''https://www.googleapis.com/books/v1/volumes'''

    query = {
        "q" : name
    }
    response = requests.get(url, params=query)
    return response.json()

