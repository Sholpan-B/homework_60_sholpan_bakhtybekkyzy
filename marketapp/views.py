from django.shortcuts import render

# Create your views here.
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect

from marketapp.forms import ProductForm, SearchForm
from marketapp.models import Product, StatusChoice


# Create your views here.
def index_view(request: WSGIRequest):
    products = Product.objects.exclude(in_stock=0).order_by('category', 'name')
    categories = StatusChoice.choices
    search_form = SearchForm()
    context = {
        'products': products,
        'search_form': search_form,
        'categories': categories
    }
    return render(request, 'index.html', context=context)


def edit_view(request, pk):
    errors = {}
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'image': product.image,
            'category': product.category,
            'in_stock': product.in_stock,
            'price': product.price
        })
        return render(request, 'product_edit.html',
                      context={
                          'product': product,
                          'choices': StatusChoice.choices,
                          'form': form
                      })
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.image = form.cleaned_data['image']
            product.category = form.cleaned_data['category']
            product.in_stock = form.cleaned_data['in_stock']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('product_detail', pk=product.pk)

        else:
            if not request.POST.get('name'):
                errors['name'] = 'Данное поле обязательно к заполнению'
            return render(request, 'product_edit.html',
                          context={
                              'product': product,
                              'choices': StatusChoice.choices,
                              'errors': errors,
                              'form': form
                          })


def detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', context={
        'product': product
    })


def delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_confirm_delete.html', context={'product': product})


def confirm_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')


def add_view(request: WSGIRequest):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'product_add.html',
                      context={
                          'choices': StatusChoice.choices,
                          'form': form
                      })
    form = ProductForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'product_add.html',
                      context={
                          'choices': StatusChoice.choices,
                          'form': form
                      })
    else:
        product = Product.objects.create(**form.cleaned_data)
        return redirect('product_detail', pk=product.pk)


def search_view(request: WSGIRequest):
    search_form = SearchForm()
    form = Product()
    search = request.GET.get('search', default='')
    products = Product.objects.exclude(in_stock=0).filter(name__icontains=search).order_by('category', 'name')
    context = {
        'products': products,
        'search_form': search_form,
        'form': form
    }
    return render(request, 'index.html', context)
