import requests
from django.shortcuts import render

def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=777fa27f36d120c5bdb8679a20318621'    
    city = 'Abidjan'

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    context ={'city_weather': city_weather}
    print(city_weather)
    return render(request, 'weather/base.html', context)
    