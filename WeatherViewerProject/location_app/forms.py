from django import forms
from django.contrib.auth.models import User
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
        # localized_fields = '__all__'
        # widgets = {
        #     'Name': forms.HiddenInput(),
        #     'Userid': forms.HiddenInput(),
        #     'Latitude': forms.HiddenInput(),
        #     'Longitude': forms.HiddenInput()
        # }

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }


    # name_city = forms.CharField(max_length=255)
    # country_code = forms.CharField(max_length=255)
    # latitude = forms.DecimalField(max_digits=18, decimal_places=5)
    # longitude = forms.DecimalField(max_digits=18, decimal_places=5)

