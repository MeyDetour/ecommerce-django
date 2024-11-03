from django.conf.urls.static import static
from django.urls import path

from ecommerce import settings
from . import views
from .views import login_view, register_view, products, add_product_to_cart, admin_create_product, admin_products, \
    admin_get_product, \
    admin_edit_product, admin_hide_product, remove_one_product_to_cart, remove_product_to_cart, \
    remove_all_product_to_cart, admin_remove_product, get_product, stripe_config, profile, get_cart, \
    admin_create_category, admin_edit_category, admin_remove_category, admin_categories, create_checkout_session, \
    cancelled, success, order_list

urlpatterns = [
    path('', products, name='index'),
    path('login', login_view, name='login'),
    path('register', register_view, name='register'),
    path('profile', profile, name='profile'),

    path('product/add/<int:id>', add_product_to_cart, name='profile'),
    path('product/get/<int:id>', get_product, name='get_product'),
    path('product/removeone/<int:id>', remove_one_product_to_cart, name='profile'),
    path('product/remove/<int:id>', remove_product_to_cart, name='profile'),
    path('cart/remove', remove_all_product_to_cart, name='profile'),
    path('order/list', order_list, name='order_list'),
    path('cart', get_cart, name='cart'),

    path('config/', stripe_config),
    path('create-checkout-session/', create_checkout_session),  # new


    path('cancelled', cancelled),
    path('success', success),

    path('admin/', admin_products, name='admin_products'),
    path('admin/product/create', admin_create_product, name='admin_create_product'),
    path('admin/product/get/<int:id>', admin_get_product, name='admin_get_product'),
    path('admin/product/edit/<int:id>', admin_edit_product, name='admin_edit_product'),
    path('admin/product/hide/<int:id>', admin_hide_product, name='admin_hide_product'),
    path('admin/product/remove/<int:id>', admin_remove_product, name='admin_remove_product'),

    path('admin/category/create', admin_create_category, name='admin_create_category'),
    path('admin/category/edit/<int:id>', admin_edit_category, name='admin_edit_category'),
    path('admin/category/remove/<int:id>', admin_remove_category, name='admin_remove_category'),
    path('admin/categories', admin_categories, name='admin_categories'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
