import sys

from config import API_KEY
from services import WeatherApiClient
from utils.formatter import format_weather
from utils.exceptions import WeatherError


def main() -> None:
    if len(sys.argv) < 2:
        """Использование python main.py <Город>"""
        return

    city = " ".join(sys.argv[1:])
    client = WeatherApiClient(API_KEY)

    try:
        weather = client.get_weather(city)
        print(format_weather(weather))
    except WeatherError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")


if __name__ == "__main__":
    main()
