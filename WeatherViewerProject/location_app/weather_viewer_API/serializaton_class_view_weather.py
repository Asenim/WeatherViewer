class SerializationClassViewWeather:
    def __init__(self, api_data, location):
        """
        Сериализуем в объекты питона отображаемые на
        фронтенде данные.
        """
        self.name_city = location.Name
        self.country_code = api_data['sys']['country']
        self.temp = api_data['main']['temp']
