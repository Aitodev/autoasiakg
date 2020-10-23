from django.shortcuts import render
from .models import Bestproduct
from cart.forms import CartAddProductForm
from cart.cart import Cart
	

def index(request):
    bestproduct = Bestproduct.objects.all()
    cart_product_form = CartAddProductForm()
    cart = Cart(request)
    context = {
        'best': bestproduct,
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