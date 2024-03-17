# Добро пожаловать на реализацию проекта "Прогноз Погоды"

Проект был реализован по ТЗ - https://github.com/zhukovsd/java-backend-learning-course/blob/main/Projects/WeatherViewer/index.md

Python версия ТЗ - https://github.com/zhukovsd/python-backend-learning-course/blob/main/Projects/WeatherViewer/index.md

### Используемые технологии
- Django
- Docker
- Docker compose
- Postgresql
- HTML CSS
- Bootstrap 5
- Django TestCase для интеграционных тестов

### Описание проекта
#### Цель проекта
- Поработать с популярным веб фреймворком Django
- Реализовать многопользовательское клиент-серверное веб приложение 
- Поработать с внешним API 

#### Основные компоненты проекта
Приложение состоит из двух основных частей:
 - Работа с Юзерами 
 - Работа с Локациями  
   - Для работы с Юзерами:
     - Реализована авторизация и регистрация при помощи встроенных инструментов Django 
     - Личный кабинет в котором будет отображаться погода добавленная пользователем к себе на страницу
     - Возможность удаления ненужных данных из личного кабинета юзера  
   - Для работы с Локациями:
     - Реализован функционал для взаимодействия с внешним API
     - Написан интерфейс для поиска локаций и добавления их в личный кабинет авторизованного пользователя

### Как запустить проект?
1. Устанавливаете git
2. Устанавливаете dokcer
3. Устанавливаете docker compose
4. Клонируете репозиторий с помощью команды git clone https://github.com/Asenim/WeatherViewer.git
5. Переходите в папку с проектом и создаете .env файл на уровне docker compose файла  
6. Выполняете команду <code>dokcer compose up</code>

#### Переменные окружения в .env файле
   - POSTGRES_PASSWORD=Пароль от БД
   - POSTGRES_USER=username от БД
   - POSTGRES_DB=Имя БД
   - TEST_POSTGRES_DB=Имя тестовой БД
   - HOST=postgresql_db #(Имя сервиса)
   - SECRET_KEY=Сгенерированный django секретный ключ
   - API_KEY_OW=Сгенерированный Open Viewer ключ API

#### Где достать ключи?
#### SECRET_KEY:
Вам нужен будет любой Django проект на вашей машине (Можете использовать текущий)  
Выполните код:   
<code>from django.core.management.utils import get_random_secret_key</code>
<code>print(get_random_secret_key())</code>  
После чего скопируйте полученный секретный ключ и и вставьте в .env SECRET_KEY
#### API_KEY_OW  
Получите API на сайте [OpenWeather](https://openweathermap.org/weather-data)  
Для этого:
- Зарегистрируйтесь на сайте
- Перейдите в личный кабинет
- Во вкладке my keys сгенерируйте собственный ключ
- Вставьте ключ в соответсвующую переменную окружения.
