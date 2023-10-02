from django.shortcuts import render, redirect
import requests
from django.views import View

from .models import City
from .forms import CityForm


# Create your views here.
class Info(View):
    def get(self, request):
        appid = '11bb77ca1670a956f5ace6631b000e0f'
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=' + appid
        cities = City.objects.all()
        all_cities = []
        for city in cities:
            res = requests.get(url.format(city.name)).json()
            city_info = {
                'city': city,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon']
            }
            all_cities.append(city_info)
        context = {
            'all_info': all_cities,
            'form': CityForm
        }
        return render(request, 'weather/index.html', context)

    def post(self, request):
        form = CityForm(request.POST)
        form.save()
        return redirect('/')

def delit(request, city):
    city = City.objects.filter(name=city)
    city.delete()
    return redirect('/')

# class Info(View):
#
#     def get(self, request):
#         appid = '11bb77ca1670a956f5ace6631b000e0f'
#         url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=' + appid
#         cities = City.objects.all()
#         all = []
#
#         async def res(city):
#             await requests.get(url.format(city.name)).json()
#
#
#         async def main():
#             tasks = [asyncio.create_task(res(city)) for city in cities]
#             o = await asyncio.gather(*tasks)
#             for city in o:
#                 city_info = {
#                     'city': city['name'],
#                     'temp': city['main']['temp'],
#                     'icon': city['weather'][0]['icon']
#                 }
#                 all.append(city_info)
#         asyncio.run(main())
#
#         # @async_to_sync
#         context = {
#             'all_info': all,
#             'form': CityForm
#         }
#         return render(request, 'weather/index.html', context)