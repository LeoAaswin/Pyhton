import requests

def weather_forecast(city,key='26631f0f41b95fb9f5ac0df9a8f43c92',units='metric'):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&units={units}'
    x = requests.get(url)
    forecast = x.json()
    return forecast



print(weather_forecast(city='kathmandu'))

