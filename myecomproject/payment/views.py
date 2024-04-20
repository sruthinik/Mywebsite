
# payment/views.py

from django.shortcuts import render, redirect
from .forms import PaymentForm
from cart.models import CartItem
from .utils import calculate_cart_total


def initiate_payment(request):
    total_price = calculate_cart_total(request.user)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            return render(request, 'payment_page.html', {'amount': amount, 'total_price': total_price})
    else:
        form = PaymentForm(initial={'amount': total_price})

    return render(request, 'payment_form.html', {'form': form, 'total_price': total_price})


def payment_success(request):
    payment_id = request.GET.get('razorpay_payment_id')
    return render(request, 'payment_success.html', {'payment_id': payment_id})


def payment_failure(request):
    payment_id = request.GET.get('razorpay_payment_id')
    return render(request, 'payment_failure.html', {'payment_id': payment_id})