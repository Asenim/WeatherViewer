from django.contrib.auth import logout
from django.shortcuts import render, redirect
from location_app.weather_viewer_API.weather_viewer_controller import WeatherViewerController
from location_app.forms import SearchWeatherForm, AddWeatherForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        forms_search = SearchWeatherForm(data=request.POST)

        if forms_search.is_valid():
            data = forms_search.cleaned_data.get('search_field')
            api_weather = WeatherViewerController()
            object_data = api_weather.search_location_by_name(data)
            context = {
                'forms_search': forms_search,
                'list_object': object_data
            }
            return render(request, 'index.html', context=context)

    else:
        forms_search = SearchWeatherForm()
        context = {
            'forms_search': forms_search
        }
        return render(request, 'index.html', context=context)


def user_logout(request):
    logout(request)
    return redirect('index')
