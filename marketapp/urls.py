from django.urls import path

from marketapp.views import index_view, add_view, edit_view, delete_view, confirm_delete, search_view, detail_view

urlpatterns = [
    path("", index_view, name='index'),
    path("product/", index_view, name='index'),
    path("product/add", add_view, name='product_add'),
    path('product/<int:pk>', detail_view, name='product_detail'),
    path('product/edit/<int:pk>', edit_view, name='product_edit'),
    path('product/delete/<int:pk>', delete_view, name='product_delete'),
    path('product/confirm_delete/<int:pk>', confirm_delete, name='confirm_delete'),
    path("product/search", search_view, name='search'),
]