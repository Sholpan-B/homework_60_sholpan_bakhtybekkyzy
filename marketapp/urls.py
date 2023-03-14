from django.urls import path

from marketapp.views.base import IndexView, IndexRedirectView
from marketapp.views.carts import add_to_cart, cart, remove_from_cart
from marketapp.views.orders import checkout_view
from marketapp.views.products import ProductDetail, ProductAddView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("product/", IndexRedirectView.as_view(), name='product_index_redirect'),
    path("product/add", ProductAddView.as_view(), name='product_add'),
    path('product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/confirm_delete/<int:pk>/', ProductDeleteView.as_view(), name='confirm_delete'),
    path('cart/add_product/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('cart/remove_from_cart/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    path('cart/order/', checkout_view, name='checkout'),
]
