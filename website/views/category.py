from itertools import product

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from website.forms import CategoryForm
from website.models import Category, Product


@user_passes_test(lambda u: u.is_superuser)
def admin_categories(request):
    categories = Category.objects.all()

    return render(request, 'website/admin/category/categories.html', {'categories': categories})


@user_passes_test(lambda u: u.is_superuser)
def admin_remove_category(request,id):
    category = Product.objects.get(id=id)
    if category.products.count() == 0:
        category.delete()
    return render(request, 'website/admin/category/categories.html', )

@user_passes_test(lambda u: u.is_superuser)
def admin_create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/admin/categories')
    form = CategoryForm()
    return render(request, 'website/admin/category/create.html', {'form': form})

@user_passes_test( lambda u: u.is_superuser)
def admin_edit_category(request, id):

    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/categories')
    form = CategoryForm(instance=category)
    return render(request, 'website/admin/category/create.html', {'form': form,'category':category})
