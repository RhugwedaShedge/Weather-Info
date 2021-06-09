from django.shortcuts import render

import urllib.request
import json
# Create your views here.

def index_view(request):

    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=16887a09cc73abe7c6e21b9d50d17bfa').read() # Contain all json data from the api

        list_of_data = json.loads(source)

        context = {
            "city": str(city),
            "country_code": str(list_of_data['sys']['country']),
            "temp": str(list_of_data['main']['temp']),
            "main": str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "icon": list_of_data['weather'][0]['icon'],

        }

        print(context)
    else:
        context = {}

    return render(request, 'index.html', context)
