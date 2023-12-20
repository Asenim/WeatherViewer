from WeatherViewerProject.settings import API_KEY_OW
from location_app.weather_viewer_API.serialization_class_location import SerializationClassLocation
import requests


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
    def add_location_in_db():
        """
        Добавляем локацию в БД.
        """
        pass


if __name__ == '__main__':
    wp = WeatherViewerController()
    datawp = wp.search_location_by_name('Saint Petersburg')
    print(datawp)
