from django.contrib.auth import logout
from django.shortcuts import render, redirect
from location_app.weather_viewer_API.weather_viewer_controller import WeatherViewerController


# Create your views here.
def index(request):
    if request.method == 'POST':
        data = request.POST
        if data['inputSearch'] == '':
            return render(request, 'index.html')
        else:
            api_weather = WeatherViewerController()
            object_data = api_weather.search_location_by_name(data['inputSearch'])
            context = {
                'list_object': object_data
            }
            return render(request, 'index.html', context=context)

    else:
        return render(request, 'index.html')


def user_logout(request):
    logout(request)
    return redirect('index')
