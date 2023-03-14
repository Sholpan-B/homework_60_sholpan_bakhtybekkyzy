from decimal import Decimal

from django import forms
from django.core.exceptions import ValidationError

from marketapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'in_stock', 'price')
        labels = {
            'name': 'Наименование',
            'description': 'Описание',
            'image': 'Фото',
            'category': 'Категория',
            'in_stock': 'Остаток',
            'price': 'Стоимость'
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 200:
            raise ValidationError('Длина превышает 200 символов!')
        return name

    def clean_in_stock(self):
        in_stock = self.cleaned_data.get('in_stock')
        if in_stock < 0:
            raise ValidationError('Остаток не может быть отрицательным')
        return in_stock

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < Decimal('0.00'):
            raise ValidationError('Стоимость не может быть отрицательной')
        return price


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')



