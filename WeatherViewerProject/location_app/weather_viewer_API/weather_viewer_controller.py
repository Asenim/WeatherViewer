from WeatherViewerProject.settings.base_settings import API_KEY_OW
from location_app.weather_viewer_API.serialization_class_location import SerializationClassLocation
from location_app.weather_viewer_API.serializaton_class_view_weather import SerializationClassViewWeather
import requests
from location_app.models import Locations
from django.contrib.auth.models import User
from decimal import Decimal


class WeatherViewerController:

    @staticmethod
    def search_location_by_name(city_name):
        """
        Ищем локацию по названию.
        """
        data = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=10&appid={API_KEY_OW}')
        data_list = data.json()
        data_list_to_object = []

        for data_dict in data_list:
            data_object = SerializationClassLocation(dictionary_data=data_dict)
            data_list_to_object.append(data_object)

        return data_list_to_object

    @staticmethod
    def add_location_in_db_actual_method(data_for_add):
        """
        Актуальный метод добавления в БД
        :param data_for_add:
        :return:
        """

        name_city = data_for_add['name_city']
        user_name = data_for_add['user_name']
        lat = float(data_for_add['lat'].replace(',', '.'))
        lon = float(data_for_add['lon'].replace(',', '.'))

        object_to_user_table = User.objects.get(username=user_name)

        initial_data = {
            'Name': name_city,
            'Userid': object_to_user_table,
            'Latitude': lat,
            'Longitude': lon
        }

        return initial_data

    def user_weather_view(self, user_name):
        """
        Используем API для формирования списка
        текущей Погоды
        :param user_name:
        :return:
        """
        list_locations = self.__select_locations_from_db(user_name=user_name)
        weather_list = []

        for location in list_locations:
            # Убираем лишние нули
            lat_decimal = Decimal(location.Latitude).normalize()
            lon_decimal = Decimal(location.Longitude).normalize()
            # Делаем запрос к api
            api_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat_decimal}&lon={lon_decimal}&appid={API_KEY_OW}&lang={"ru"}&units=metric')
            json_api_data = api_data.json()
            # Сериализуем объект и добавляем в список для дальнейшего отображения
            object_weather = SerializationClassViewWeather(json_api_data, location)
            weather_list.append(object_weather)

        return weather_list

    @staticmethod
    def __select_locations_from_db(user_name):
        """
        Метод позволяет достать все локации из БД
        принадлежащие определенному пользователю.
        :return:
        """
        username = user_name
        user = User.objects.get(username=username)
        list_objects_locations = Locations.objects.filter(Userid=user)

        return list_objects_locations

    @staticmethod
    def delete_location_form_db(id_record, user_name):
        user = User.objects.get(username=user_name)
        object_locations = Locations.objects.filter(id=id_record).filter(Userid=user)

        object_locations.delete()
