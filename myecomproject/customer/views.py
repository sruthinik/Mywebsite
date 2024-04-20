

# Create your views here.
# customers/views.py
from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("order_placing_page")
    else:
        form = CustomerForm()
    return render(request, 'customer.html', {'form': form})

