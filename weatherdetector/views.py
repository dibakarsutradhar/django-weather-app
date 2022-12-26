from django.shortcuts import render
from dotenv import load_dotenv
import os
import json
import urllib.request

load_dotenv()

WEATHER_API = os.getenv("OPEN_WEATHER_API_KEY")

# Create your views here.
def index(request):
	if request.method == 'POST':
		city = request.POST['city']
		res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID='+WEATHER_API).read()
		json_data = json.loads(res)
		data = {
			"country_code": str(json_data['sys']['country']),
			"coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
			"temp": str(json_data['main']['temp'])+'k',
			"pressure": str(json_data['main']['pressure']),
			"humidity": str(json_data['main']['humidity']),
		}
	else:
		city = ''
		data = {}
	return render(request, 'index.html', {'city': city, 'data': data})