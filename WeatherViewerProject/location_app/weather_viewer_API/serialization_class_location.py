class SerializationClassLocation:
    def __init__(self, dictionary_data):
        """
        :param dictionary_data: Словарь с данными.

        Поля класса:
            name_city: имя города.
            country_code: код страны.
            lat: широта локации.
            lon: долгота локации.
        """
        self.name_city = dictionary_data['name']
        self.country_code = dictionary_data['country']
        self.lat = dictionary_data['lat']
        self.lon = dictionary_data['lon']
