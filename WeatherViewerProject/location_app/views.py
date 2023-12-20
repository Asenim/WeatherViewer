from django.shortcuts import render, redirect
from location_app.weather_viewer_API.weather_viewer_controller import WeatherViewerController

# Create your views here.


def weather_viewer_find(request):
    """
    Ищем данные о городе и отображаем их на странице.
    :return:
    """
    # data = request.POST
    # api_weather = WeatherViewerController()
    # object_data = api_weather.search_location_by_name(data['inputSearch'])
    # context = {
    #     'name_city': object_data.name_city,
    #     'country_code': object_data.country_code,
    #     'lat': object_data.lat,
    #     'lon': object_data.lon
    # }
    # # context = {'inp': 'hi!'}
    # # print(data['inputSearch'])
    # return render(request, 'index.html', context=context)
    # # return redirect('index')


def weather_viewer_add(request):
    """
    Добавляем данные о городе в БД
    :return:
    """
    pass
