import time
import django.db.utils
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestAuthorization(TestCase):
    def setUp(self) -> None:
        self.data_for_user_create = {
            'username': 'Giga',
            'password1': 'Chad300l',
            'password2': 'Chad300l'
        }
        self.data_for_user_authorization = {
            'username': 'Giga',
            'password': 'Chad300l'
        }
        self.client.post(reverse('user_registration'), data=self.data_for_user_create)
        self.response_authorization = self.client.post(reverse('user_authorization'),
                                                       data=self.data_for_user_authorization)

    def test_user_authorization(self):
        """
        Тестируем корректность авторизации пользователя.
        """
        # Произошел ли редирект?
        self.assertEqual(self.response_authorization.status_code, 302)
        self.assertEqual(self.response_authorization.url, reverse('index'))
        # Переходим в личный кабинет
        response_personal_area_in_site = self.client.get(reverse('user_locations'))
        self.assertEqual(response_personal_area_in_site.status_code, 200)
        self.assertIsNotNone(self.client.session.session_key)

    def test_session_expiration(self):
        """
        Тестируем завершается ли работа сессии через
        некоторый промежуток времени.
        """
        # Тест на факт наличие активной сессии
        self.client.get(reverse('user_locations'))
        self.assertIsNotNone(self.client.session.session_key)
        # Тест на отсутствие активной сессии
        time.sleep(12)
        self.client.get(reverse('user_locations'))
        self.assertIsNone(self.client.session.session_key)
