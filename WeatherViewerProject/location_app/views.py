from django.shortcuts import render, redirect, HttpResponse
from location_app.weather_viewer_API.weather_viewer_controller import WeatherViewerController

# Create your views here.


def view_user_locations(request):
    """
    Показывает погоду локаций добавленных на аккаунт.
    :return:
    """
    user_name = request.user.username

    wvc = WeatherViewerController()
    list_data_from_db = wvc.user_weather_view(user_name=user_name)

    context = {
        'locations_list': list_data_from_db
    }
    return render(request, 'location_templates/user_added_locations.html', context=context)


def weather_viewer_delete(request):
    """
    Удаляет данные добавленных локаций из БД
    :param request:
    :return:
    """
    if request.method == 'POST':
        id_record = request.POST['id_db']
        username = request.POST['user_name']
        print(id_record, username)
        wwc = WeatherViewerController()
        wwc.delete_location_form_db(id_record=id_record, user_name=username)

    return redirect('user_locations')


def weather_viewer_add(request):
    """
    Добавляем данные о городе в БД
    :return:
    """
    data = request.POST
    # try:
    wwc = WeatherViewerController()
    wwc.add_location_in_db(data)

    return redirect('index')
    # except Exception:
    #     string_error = {'errors': 'Вы уже добавили данные с такими координатами'}
    #
    #     return render(request, 'location_templates/insert_error.html', context=string_error)
