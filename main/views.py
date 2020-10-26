from cart.forms import CartAddBestproductForm
from django.shortcuts import render
from .models import Bestproduct
from cart.cart import Cart


def index(request):
    products = Bestproduct.objects.all()
    cart_product_form = CartAddBestproductForm()
    cart = Cart(request)
    context = {
        'best': products,
        'cart': cart,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def shop(request):
    return render(request, 'main/product.html')


def contact(request):
    return render(request, 'main/contact.html')
