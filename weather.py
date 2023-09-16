import requests
import datetime
from dotenv import load_dotenv
import os
from dataclasses import dataclass

@dataclass
class WeatherData:
    main: str
    desc: str
    icon: str
    temp: float
    city_name: str
    feels_like: str
    temp_low: str
    temp_high: str
    humidity: str
    wind: str

load_dotenv()
API_KEY = os.getenv('API_KEY')

def get_lat_long(city_name, state_code, country_code, API_KEY):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=&appid={API_KEY}').json()
    lat, long = response[0].get('lat'), response[0].get('lon')
    return lat, long

def get_weather(city_name, state_code, country_code, API_KEY):
    lat, lon = get_lat_long(city_name, state_code, country_code, API_KEY)
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial').json()
    data = WeatherData(
        main=response.get('weather')[0].get('main'),
        desc=response.get('weather')[0].get('description'),
        icon=response.get('weather')[0].get('icon'),
        temp=response.get('main').get('temp'),
        temp_low=response.get('main').get('temp_min'),
        temp_high=response.get('main').get('temp_max'),
        city_name=response.get('name'),
        feels_like=response.get('main').get('feels_like'),
        humidity=response.get('main').get('humidity'),
        wind=response.get('wind').get('speed')
    )
    data.feels_like = round(data.feels_like)
    data.temp = round(data.temp)
    data.temp_low = round(data.temp_low)
    data.temp_high = round(data.temp_high)
    return data

def main(city_name, state_name, country_name):
    data = get_weather(city_name, state_name, country_name, API_KEY)
    return data

