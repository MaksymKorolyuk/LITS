import requests


def api_key():
    api_key = '777d8f493aea54c7de97432b49b4954a'
    return api_key


def get_weather(api_key, location):
    lang = 'ua'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&lang={}&units=metric&appid={}".format(location,
                                                                                                      lang,
                                                                                                      api_key)
    response = requests.get(url=url)

    return response.json()


def weather():
    location = input('Enter the city name: ')
    weather_data = get_weather(api_key(), location)

    print(f"""
Координати місця знаходження об'єкту:
    Довгота: {weather_data['coord']['lon']},
    Широта: {weather_data['coord']['lat']},
Погода:
    Погода: {weather_data['weather'][0]['description']},
    Температура: {weather_data['main']['temp']} градусів Цельсія,
    Тиск: {weather_data['main']['pressure']} hPa,
    Вологість: {weather_data['main']['humidity']} %,
""")


weather()
