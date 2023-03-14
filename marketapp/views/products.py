from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from marketapp.forms import ProductForm
from marketapp.models import Product
from marketapp.models.orders import OrderProduct, Order


class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    model = Product


class ProductAddView(CreateView):
    template_name = 'product_add.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    template_name = 'product_edit.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_product = OrderProduct.objects.create(product=product)
    order = Order.objects.filter()