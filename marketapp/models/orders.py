from django.db import models


class Order(models.Model):
    products = models.ManyToManyField('marketapp.Product', through='OrderProduct', verbose_name="Товары")
    user_name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Имя пользователя')
    phone = models.CharField(max_length=100, null=False, blank=False, verbose_name='Телефон')
    address = models.CharField(max_length=300, null=False, blank=False, verbose_name='Адрес')
    ordered_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")

    def __str__(self):
        return f"Заказ клиента: {self.user_name} ({self.ordered_at.strftime('%Y-%m-%d %H:%M:%S')})"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderProduct(models.Model):
    order = models.ForeignKey('marketapp.Order', related_name='order_products', on_delete=models.CASCADE,
                              verbose_name='Заказ')
    product = models.ForeignKey(
        'marketapp.Product',
        related_name='products_order',
        on_delete=models.CASCADE,
        verbose_name='Товар'
    )
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

    def str(self):
        return f'{self.quantity} x {self.product.name} для заказа клиента {self.order.user_name}'

    class Meta:
        verbose_name = 'Заказанные товары'
        verbose_name_plural = 'Заказанные товары'