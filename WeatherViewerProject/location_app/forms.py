from django import forms
from location_app.models import Locations
from django.core.exceptions import NON_FIELD_ERRORS


class SearchWeatherForm(forms.Form):
    """
    Класс формы для поиска локаций
    """
    search_field = forms.CharField(max_length=255, label='', widget=forms.TextInput(
        attrs={
            'id': 'inputSearch', 'name': 'inputSearch',
            'class': 'form-control', 'placeholder': 'Поиск'
        }
    ))


class AddWeatherForm(forms.ModelForm):
    """
    Класс формы для добавления локаций
    """
    class Meta:
        model = Locations
        fields = ['Name', 'Userid', 'Latitude', 'Longitude']

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': 'Эти данные уже существуют в таблице локаций'
            }
        }
