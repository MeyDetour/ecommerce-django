
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

from website.forms import ObjctForm
from website.models import Product


def products(request):
    return render(request, 'website/client/product/products.html',{'products':Product.objects.all()})



#========================================================ADMIN
@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    return render(request, 'website/admin/product/products.html',{'products':Product.objects.all()})

@user_passes_test(lambda u: u.is_superuser)
def admin_create_product(request):
    if request.method == 'POST':
        form = ObjctForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return HttpResponseRedirect('/')
    form = ObjctForm
    return render(request, 'website/admin/product/create.html',{'form':form})

@user_passes_test(lambda u: u.is_superuser)
def admin_get_product(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'website/admin/product/show.html',{'product':product})

@user_passes_test(lambda u: u.is_superuser)
def admin_edit_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ObjctForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
             form.save()
             return HttpResponseRedirect('/admin/product/get/'+str(id))
    form = ObjctForm(instance=product)
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

