from django.test import TestCase
from django.urls import reverse
from location_app.weather_viewer_API.weather_viewer_controller import WeatherViewerController
from location_app.weather_viewer_API.serialization_class_location import SerializationClassLocation
from location_app.models import Locations
from django.contrib.auth.models import User


class TestWeatherViewerAPI(TestCase):
    def setUp(self) -> None:
        # Инициализация Сервиса
        self.wvc = WeatherViewerController()
        self.search_data = {
            'search_field': 'Тбилиси'
        }
        self.testing_data = ('Tbilisi', 'GE')
        # Создание Юзера для работы с сервисом
        self.data_for_user_create = {
            'username': 'Giga',
            'password1': 'Chad300l',
            'password2': 'Chad300l'
        }
        self.data_for_user_authorization = {
            'username': 'Giga',
            'password': 'Chad300l'
        }
        self.client.post(reverse('user_registration'), self.data_for_user_create)
        self.response_authorization = self.client.post(reverse('user_authorization'),
                                                       self.data_for_user_authorization)
        # Добавление данных в БД и подготовка к этому
        self.response_search_view = self.client.post(reverse('index'), data=self.search_data)
        self.data_for_add_db = {
            'name_city': self.response_search_view.context['list_object'][0].name_city,
            'user_name': self.data_for_user_authorization['username'],
            'lat': self.response_search_view.context['list_object'][0].lat,
            'lon': self.response_search_view.context['list_object'][0].lon
        }
        self.response_data_add_db = self.client.post(reverse('viewer_add'), data=self.data_for_add_db)

    def test_views_index_search_location(self):
        """
        Тестирование вьюху поиска локаций.
        """
        checked_data = (self.response_search_view.context['list_object'][0].name_city,
                        self.response_search_view.context['list_object'][0].country_code)

        self.assertEqual(self.response_search_view.status_code, 200)
        self.assertEqual(checked_data, self.testing_data)

    def test_search_location(self):
        """
        Тестируем поиск локаций.
        """
        list_search_locations = self.wvc.search_location_by_name(self.search_data['search_field'])
        first_object_is_from_list = list_search_locations[0]
        self.assertTrue(isinstance(list_search_locations, list))
        self.assertTrue(isinstance(first_object_is_from_list, SerializationClassLocation))
        self.assertEqual((first_object_is_from_list.name_city, first_object_is_from_list.country_code),
                         self.testing_data)

    def test_add_location(self):
        """
        Тестируем добавление локаций в БД.
        :return:
        """
        # Проверяем добавление данных (отрабатывание логики в случае если данные успешно добавлены в БД)
        self.assertEqual(self.response_data_add_db.status_code, 302)
        self.assertEqual(self.response_data_add_db.url, reverse('user_locations'))
        # Проверяем что данные существуют в таблице
        user_object = User.objects.get(username=self.data_for_user_authorization['username'])
        location = Locations.objects.get(Userid=user_object, Name=self.testing_data[0])
        self.assertEqual((location.Name, location.Userid.username), (self.testing_data[0],
                                                                     self.data_for_user_authorization['username']))

    def test_delete_location(self):
        """
        Тестируем удаляется ли локация из БД
        :return:
        """
        # Проверяем что данные существуют в таблице
        user_object = User.objects.get(username=self.data_for_user_authorization['username'])
        location = Locations.objects.get(Userid=user_object, Name=self.testing_data[0])
        self.assertEqual((location.Name, location.Userid.username), (self.testing_data[0],
                                                                     self.data_for_user_authorization['username']))
        # Удаляем данные из таблицы
        data_for_delete = {
            'id_db': location.id,
            'user_name': location.Userid.username
        }
        self.client.post(reverse('viewer_delete'), data=data_for_delete)
        # Проверяем что данные удалены
        self.assertEqual(Locations.objects.filter(Name=self.testing_data[0]).count(), 0)
        with self.assertRaises(Locations.DoesNotExist):
            Locations.objects.get(Userid=user_object, Name=self.testing_data[0])

    def test_deleting_another_users_data(self):
        """
        Тестируем обработку ошибки при удалении чужой записи.
        :return:
        """
        # Проверяем что данные существуют в таблице
        user_object = User.objects.get(username=self.data_for_user_authorization['username'])
        location = Locations.objects.get(Userid=user_object, Name=self.testing_data[0])
        self.assertEqual((location.Name, location.Userid.username), (self.testing_data[0],
                                                                     self.data_for_user_authorization['username']))
        # Удаляем данные из таблицы
        data_for_delete = {
            'id_db': location.id,
            'user_name': 'Sergey'
        }
        response_delete = self.client.post(reverse('viewer_delete'), data=data_for_delete)
        # Проверяем что вьюха возвращает контекст с ошибкой
        self.assertTrue('errors' in response_delete.context[0])
        # Проверяем что объект находится в БД
        self.assertEqual(Locations.objects.filter(Userid=user_object, Name=self.testing_data[0]).count(), 1)
