from django.db import models
from django.db.models import TextChoices


# Create your models here.
class StatusChoice(TextChoices):
    OTHER = 'OTHER', 'Разное'
    LAPTOPS = 'LAPTOP', 'Ноутбуки'
    SMARTPHONES = 'SMARTPHONES', 'Смартфоны'
    FOR_KITCHEN = 'FOR_KITCHEN', 'Техника для кухни'


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование товара')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание")
    image = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Фото товара')
    category = models.CharField(
        choices=StatusChoice.choices,
        max_length=100,
        null=False,
        blank=False,
        default=StatusChoice.OTHER,
        verbose_name='Категория'
    )
    in_stock = models.PositiveIntegerField(null=False, blank=False, verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость')

    def __str__(self):
        return f"{self.name} - {self.description} - {self.category} - {self.price}"
