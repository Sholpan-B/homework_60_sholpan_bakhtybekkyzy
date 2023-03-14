from django.contrib import admin

from marketapp.models import ProductInCart, Order
from marketapp.models.orders import OrderProduct
from marketapp.models import Product

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductInCart)
admin.site.register(Order)
admin.site.register(OrderProduct)
