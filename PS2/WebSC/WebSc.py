import requests
from bs4 import BeautifulSoup
import json
import re

url = 'https://en.wikipedia.org/wiki/List_of_N%C3%BCrburgring_Nordschleife_lap_times'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontre a tabela que contém as informações
lap_time_table = soup.find('table', {'class': 'wikitable'})

# Inicialize listas para cada campo
length_list = []
time_list = []
vehicle_list = []
driver_list = []
date_list = []
notes_list = []

# Percorra as linhas da tabela
for row in lap_time_table.find_all('tr')[1:]:  # Pule a primeira linha (cabeçalho)
    columns = row.find_all('td')
    if len(columns) == 6:  # Certifique-se de que existam 6 colunas
        length_list.append(columns[0].text.strip())
        time_list.append(columns[1].text.strip())
        vehicle_list.append(columns[2].text.strip())
        driver_list.append(columns[3].text.strip())
        date_list.append(columns[4].text.strip())
        notes_list.append(columns[5].text.strip())

# Crie três listas para separar os dados com base no tempo
under_7_minutes = []
between_7_and_8_minutes = []
between_8_and_10_minutes = []

for i in range(len(time_list)):
    lap_time = re.split(r'[:.]', time_list[i])
    minutes = int(lap_time[0])
    seconds = int(lap_time[1])
    milliseconds = int(lap_time[2]) if len(lap_time) > 2 else 0

    total_seconds = (minutes * 60) + seconds + (milliseconds / 1000)

    if total_seconds < 420:  # Menos de 7 minutos (7 minutos = 420 segundos)
        under_7_minutes.append({
            "Length": length_list[i],
            "Time": time_list[i],
            "Vehicle": vehicle_list[i],
            "Driver": driver_list[i],
            "Date": date_list[i],
            "Notes": notes_list[i]
        })
    elif 420 <= total_seconds < 480:  # Entre 7 e 8 minutos
        between_7_and_8_minutes.append({
            "Length": length_list[i],
            "Time": time_list[i],
            "Vehicle": vehicle_list[i],
            "Driver": driver_list[i],
            "Date": date_list[i],
            "Notes": notes_list[i]
        })
    elif 480 <= total_seconds < 600:  # Entre 8 e 10 minutos
        between_8_and_10_minutes.append({
            "Length": length_list[i],
            "Time": time_list[i],
            "Vehicle": vehicle_list[i],
            "Driver": driver_list[i],
            "Date": date_list[i],
            "Notes": notes_list[i]
        })

# Salve as listas em arquivos JSON
with open('under_7_minutes.json', 'w') as file:
    json.dump(under_7_minutes, file, indent=4)

with open('between_7_and_8_minutes.json', 'w') as file:
    json.dump(between_7_and_8_minutes, file, indent=4)

with open('between_8_and_10_minutes.json', 'w') as file:
    json.dump(between_8_and_10_minutes, file, indent=4)
