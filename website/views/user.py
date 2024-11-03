from pprint import pprint

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from ecommerce import settings
from website.forms import UserForm
from website.models import Product, Order
from website.services.cart_services import Cart_service


def profile(request):
    if not request.user.is_authenticated:
        return  HttpResponseRedirect('/login')
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    form = UserForm()
    return  render(request, 'website/client/user/index.html',{'form':form})

def get_cart(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    cart_service =  Cart_service(request)
    cart_data = cart_service.get_cart()
    cart = []
    for product_id,quantity in  cart_data.items():
        product = Product.objects.get(id=product_id)
        cart.append({
            'product': product,
            'quantity': int(quantity)
        })
    return render(request, 'website/client/user/cart.html', {'cart':cart})

def order_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    orders = Order.objects.filter(user=request.user)
    return render(request, 'website/client/user/orders.html', {'orders':orders})


def recap_cart(request):
    cart_service = Cart_service(request)
    cart_data = cart_service.get_cart()
    cart = []
    total = 0
    for product_id, quantity in cart_data.items():
        product = Product.objects.get(id=product_id)
        total += int(quantity)*product.price
        cart.append({
            'product': product,
            'quantity': int(quantity)
        })
    return render(request, 'website/client/user/recap_cart.html',{
        'cart':cart,
        "total":total
    })

