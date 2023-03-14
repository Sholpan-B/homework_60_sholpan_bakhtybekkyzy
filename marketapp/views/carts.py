from django.shortcuts import redirect, render

from marketapp.models import Product, ProductInCart


def add_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    quantity = int(request.POST.get('quantity', 1))
    if product.in_stock >= quantity:
        try:
            item = ProductInCart.objects.get(product=product)
            if item.quantity + quantity <= product.in_stock:
                item.quantity += quantity
                item.save()
        except ProductInCart.DoesNotExist:
            if quantity <= product.in_stock:
                item = ProductInCart(product=product, quantity=quantity)
                item.save()
    return redirect(request.META.get('HTTP_REFERER'))


def cart(request):
    products = ProductInCart.objects.all()
    total = 0
    for product in products:
        total += product.product.price * product.quantity
        product.amount = product.product.price * product.quantity
    return render(request, 'cart.html', {'products': products, 'total': total, 'amount': product.amount})


def remove_from_cart(request, product_id=None):
    product = ProductInCart.objects.get(id=product_id)
    if product.quantity > 1:
        product.quantity -= 1
        product.save()
    else:
        product.delete()
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)
