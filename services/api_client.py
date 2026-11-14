import requests

from models import Weather
from utils import ApiError, CityNotFoundError


class WeatherApiClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city: str) -> Weather:
            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric",
                "lang": "ru",
            }

            try:
                responce = requests.get(self.base_url, params=params, timeout=10)
                responce.raise_for_status()
            except requests.exceptions.HTTPError:
                if responce.status_code == 404:
                    raise CityNotFoundError(f"Город {city} не найден")
                raise ApiError(f"Ошибка API: {responce.status_code}")
            except requests.exceptions.RequestException as e:
                raise ApiError(f"Ошибка сети: {e}")

            data = responce.json()

            return Weather(
                city=data["name"],
                temperature=data["main"]["temp"],
                feels_like=data["main"]["feels_like"],
                humidity=data["main"]["humidity"],
                wind_speed=data["wind"]["speed"],
                description=data["weather"][0]["description"],
            )