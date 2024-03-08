import django.db.utils
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.


class TestRegistration(TestCase):
    def setUp(self) -> None:
        self.data_for_registration = {
            'username': 'Giga',
            'password1': 'Chad300l',
            'password2': 'Chad300l'
        }

    def test_add_registration_user(self):
        """
        Проверка на корректность добавления данных в БД
        :return:
        """
        test_response = self.client.post(reverse('user_registration'), data=self.data_for_registration)
        # Проверка на то что редирект произошел
        self.assertEqual(test_response.status_code, 302)
        self.assertRedirects(test_response, reverse('user_authorization'))
        # Проверяем что юзер был добавлен через форму
        expected_data = 'Giga'
        verifiable_data = User.objects.get(username=expected_data)
        self.assertEqual(str(verifiable_data), expected_data)

    def test_except_double_username_added(self):
        """
        Проверка на исключения при добавлении данных с
        одинаковым username в БД
        :return:
        """
        data_to_throw_an_exception = {
            'username': 'Giga',
            'password1': 'Chad300las',
            'password2': 'Chad300las'
        }
        # добавляем пользователя через форму
        self.client.post(reverse('user_registration'), data=self.data_for_registration)
        # Повторно добавляем пользователя через форму
        test_response_registration_form = self.client.post(reverse('user_registration'),
                                                           data=data_to_throw_an_exception)
        # Проверка корректности работы формы
        self.assertEqual(test_response_registration_form.status_code, 200)
        self.assertTemplateUsed(test_response_registration_form, 'users_templates/user_registration.html')
        # Тестируем на уровне добавления в БД
        with self.assertRaises(django.db.utils.IntegrityError):
            User.objects.create_user(username='Giga', password=data_to_throw_an_exception['password1'])
