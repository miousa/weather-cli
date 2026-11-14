from dataclasses import dataclass


@dataclass
class Weather:
    city: str
    temperature: float
    feels_like: float
    humidity: int
    wind_speed: float
    description: str

    def __str__(self) -> str:
        return (
            f"Погода в {self.city}:\n"
            f"🌡️ Температура: {self.temperature}°C (ощущается как {self.feels_like}°C)\n"
            f"📝 {self.description.capitalize()}\n"
            f"💧 Влажность: {self.humidity}%\n"
            f"💨 Ветер: {self.wind_speed} м/с"
        )