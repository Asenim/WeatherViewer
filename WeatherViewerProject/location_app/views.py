from django.shortcuts import render, redirect
from location_app.weather_viewer_API.weather_viewer_controller import WeatherViewerController
from location_app.forms import AddWeatherForm

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

    if request.method == 'POST':
        data = request.POST
        wwc = WeatherViewerController()
        initial_data = wwc.add_location_in_db_actual_method(data_for_add=data)

        form_add_data = AddWeatherForm(initial_data)

        # print(form_add_data.is_valid())
        # print(initial_data)
        # print(form_add_data.errors)

        if form_add_data.is_valid():
            form_add_data.save()
            return redirect('user_locations')

        else:
            """
            Идея - Сделать render index html и добавить отображение всех необходимых форм
            прямо тут (Search + Locations)
            Либо Вынести Форму добавления в БД на уровень выше (view index) и обрабатывать ошибку
            там (У этого метода есть Проблема)
            """
            return redirect('index')
