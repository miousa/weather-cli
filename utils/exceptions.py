class WeatherError(Exception):
    """Базовый класс наших ошибок"""
    pass


class CityNotFoundError(WeatherError):
    """Город не найден"""
    pass


class ApiError(WeatherError):
    """Ошибка API (ключ не работает, сервер упал)"""
    pass