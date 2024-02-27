class SerializationClassViewWeather:
    def __init__(self, api_data, location):
        """
        Сериализуем в объекты питона отображаемые на
        фронтенде данные.

        Параметры:
            api_data - json или словарь с данными из внешнего api
            location - список локаций добавленные в нашу БД с необходимыми нам полями
                для дальнейшего отображения (корректный ID можно получить только из БД)
        Поля класса:
            self.ID = Для удаления, получаем из БД
            self.name_city = Для отображения, получаем от АПИ погоды
            self.country_code = Для отображения, получаем от АПИ погоды
            self.temp = Для отображения, получаем от АПИ погоды
        """
        self.ID = location.id
        self.name_city = api_data['name']
        self.country_code = api_data['sys']['country']
        self.temp = api_data['main']['temp']
