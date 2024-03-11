from django.shortcuts import render, redirect
from location_app.weather_viewer_API.weather_viewer_controller import WeatherViewerController
from location_app.forms import AddWeatherForm

# Create your views here.


def view_user_locations(request):
    """
    Показывает погоду локаций добавленных на аккаунт.
    :return:
    """
    if request.user.is_authenticated:
        user_name = request.user.username
        session = request.session
        print(session.keys())

        wvc = WeatherViewerController()
        list_data_from_db = wvc.user_weather_view(user_name=user_name)

        context = {
            'locations_list': list_data_from_db
        }
        return render(request, 'location_templates/user_added_locations.html', context=context)
    else:
        error_authorization = 'К сожалению вы не авторизованы, вам следует пройти процесс авторизации заново.'
        return render(request, 'location_templates/error_template.html', context={'errors': error_authorization})


def weather_viewer_delete(request):
    """
    Удаляет данные добавленных локаций из БД
    :param request:
    :return:
    """
    if request.method == 'POST':
        id_record = request.POST['id_db']
        username = request.POST['user_name']
        username_in_post_request = request.user.username

        # Проверка на корректность пользователя сделавшего запрос
        if username == username_in_post_request:
            wwc = WeatherViewerController()
            wwc.delete_location_form_db(id_record=id_record, user_name=username)

            return redirect('user_locations')
        else:
            error_delete = 'Ах ты... хитрый диванный хакер, нельзя удалять чужие данные из консоли разработчика'
            return render(request, 'location_templates/error_template.html', context={'errors': error_delete})


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

        if form_add_data.is_valid():
            form_add_data.save()
            return redirect('user_locations')

        else:
            error_form = form_add_data.non_field_errors()
            return render(request, 'location_templates/error_template.html', context={'errors': error_form})
