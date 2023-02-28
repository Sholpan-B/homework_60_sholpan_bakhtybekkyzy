from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from marketapp.models import StatusChoice


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Наименование")
    description = forms.CharField(max_length=2000, required=False, label="Описание", widget=widgets.Textarea)
    image = forms.CharField(max_length=3000, required=False, label="Фото")
    category = forms.ChoiceField(choices=StatusChoice.choices, required=True, label="Категория")
    in_stock = forms.IntegerField(required=True, label='Остаток')
    price = forms.DecimalField(required=True, min_value=1, max_digits=7, decimal_places=2, label='Стоимость')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise ValidationError('Имя должно быть длиннее 3 символов!')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "@" not in email:
            raise ValidationError("Email должен содержать '@'!")
        return email


class SearchForm(forms.Form):
    search = forms.CharField(
        label="Поиск",
        max_length=300,
        required=False,
    )
