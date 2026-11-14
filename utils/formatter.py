class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def format_weather(weather) -> str:
    # Эмодзи для разных температур
    if weather.temperature > 25:
        emoji = "🔥"
    elif weather.temperature > 10:
        emoji = "☀️"
    elif weather.temperature > 0:
        emoji = "🌥️"
    else:
        emoji = "❄️"

    return f"""
{Colors.BOLD}{Colors.BLUE}=== Погода в {weather.city} ==={Colors.ENDC}
{emoji} Температура: {Colors.GREEN}{weather.temperature}°C{Colors.ENDC}
🤔 Ощущается как: {weather.feels_like}°C
💧 Влажность: {weather.humidity}%
💨 Ветер: {weather.wind_speed} м/с
📝 Описание: {weather.description.capitalize()}
"""