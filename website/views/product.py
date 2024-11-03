
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.termcolors import RESET

from website.forms import ProductForm
from website.models import Product
from website.services.cart_services import Cart_service


def products(request):
    return render(request, 'website/client/product/products.html',{'products':Product.objects.all()})

def get_product(request, id):
    return render(request, 'website/client/product/product.html', {'product': Product.objects.get(id=id)})


def add_product_to_cart(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    cart_service = Cart_service(request)
    cart_service.add(id,request)
    return  HttpResponseRedirect('/cart')
def remove_one_product_to_cart(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    cart_service = Cart_service(request)
    cart_service.remove_one_of_product(id, request)

    return  HttpResponseRedirect('/cart')
def remove_product_to_cart(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')

    cart_service = Cart_service(request)
    cart_service.remove_product(id, request)

    return  HttpResponseRedirect('/cart')
def remove_all_product_to_cart(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')

    cart_service = Cart_service(request)
    cart_service.remove_products( request)

    return  HttpResponseRedirect('/cart')


#========================================================ADMIN
@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    return render(request, 'website/admin/product/products.html',{'products':Product.objects.all()})

@user_passes_test(lambda u: u.is_superuser)
def admin_create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return HttpResponseRedirect('/')
    form = ProductForm
    return render(request, 'website/admin/product/create.html',{'form':form})

@user_passes_test(lambda u: u.is_superuser)
def admin_get_product(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'website/admin/product/show.html',{'product':product})

@user_passes_test(lambda u: u.is_superuser)
def admin_edit_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
             form.save()
             return HttpResponseRedirect('/admin/product/get/'+str(id))
    form = ProductForm(instance=product)
    return render(request, 'website/admin/product/create.html',{'form':form})

@user_passes_test(lambda u: u.is_superuser)
def admin_hide_product(request,id):
    product = Product.objects.get(id=id)
    if product.is_hidden:
        product.is_hidden = False
    else :
        product.is_hidden = True
    product.save()
    return HttpResponseRedirect('/admin/')

@user_passes_test(lambda u: u.is_superuser)
def admin_remove_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect('/admin/')

