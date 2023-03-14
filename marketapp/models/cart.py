from django.db import models


class ProductInCart(models.Model):
    product = models.ForeignKey('marketapp.Product', verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', null=False, blank=False, default=0)

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'