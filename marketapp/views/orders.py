from django.shortcuts import redirect, render

from marketapp.models import Order
from marketapp.models.orders import OrderProduct


def checkout_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        order = Order.objects.create(
            user_name=name,
            address=address,
            phone=phone
        )

        for item in request.session['cart']:
            OrderProduct.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity']
            )

        request.session['cart'] = []
        return redirect('order_success')

    return render(request, 'partial/order.html')
