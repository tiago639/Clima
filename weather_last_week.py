import requests
import pandas as pd
from datetime import datetime, timedelta

# Configurações
API_KEY = '2150c9d6f4c84e0689a135255252307'  # <-- coloque sua chave da WeatherAPI
CITY = 'Sao Paulo'
BASE_URL = 'http://api.weatherapi.com/v1/history.json'

# Lista para armazenar os dados
weather_data = []

# Últimos 7 dias
for i in range(7):
    date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
    params = {
        'key': API_KEY,
        'q': CITY,
        'dt': date
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        day = data['forecast']['forecastday'][0]['day']
        weather_data.append({
            'date': date,
            'avg_temp_c': day['avgtemp_c'],
            'max_temp_c': day['maxtemp_c'],
            'min_temp_c': day['mintemp_c'],
            'condition': day['condition']['text'],
            'precip_mm': day['totalprecip_mm'],
            'humidity': day['avghumidity']
        })
    else:
        print(f'Erro ao buscar dados para {date}: {response.text}')

# Converter em DataFrame
df = pd.DataFrame(weather_data)

# Salvar em Excel
df.to_excel('weather_last_week.xlsx', index=False)
print("Arquivo Excel salvo com sucesso!")
