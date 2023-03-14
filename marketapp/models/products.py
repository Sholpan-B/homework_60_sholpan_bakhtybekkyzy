from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


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
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    is_deleted = models.BooleanField(verbose_name='удалено', null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)

    def __str__(self):
        return f"{self.name} - {self.description} - {self.category} - {self.price}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'