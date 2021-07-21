import requests, datetime


def background_image(time):
    hour = int(time)
    if 9 < hour < 17:
        return 'day'
    elif 20 < hour <= 23 or 0 < hour < 6:
        return 'night'
    else:
        return 'evening-morning'


def city_id(name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={name}&appid=cb91583deb2b39ac8ad3714e2e3b9a70'
    response = requests.get(url)
    if response.json()['cod'] == '404':
        return None

    return response.json()['id'], response.json()['name']


def weather(name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={name}&appid=cb91583deb2b39ac8ad3714e2e3b9a70'
    response = requests.get(url)

    state = response.json()['weather'][0]['main']
    temperature = round(response.json()['main']['temp'] - 273.15)
    city_name = response.json()['name']
    id_city = response.json()['id']
    timezone = response.json()['timezone']
    tz = datetime.datetime.utcnow() + datetime.timedelta(seconds=timezone)
    image = background_image(tz.strftime('%H'))
    weather_data = {'state': state, 'temperature': temperature,
                    'city_name': city_name, 'timezone': image, 'id': id_city}
    return weather_data




