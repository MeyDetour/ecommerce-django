from django.conf.urls.static import static
from django.urls import path

from ecommerce import settings
from . import views
from .views import login_view, register_view, products, admin_create_product, admin_products, admin_get_product, \
    admin_edit_product, admin_hide_product
from .views.user import profile

urlpatterns = [
    path('', products, name='index'),
    path('login', login_view , name='login'),
    path('register', register_view, name='register'),
    path('profile', profile, name='profile'),
    path('admin/', admin_products, name='admin_products'),
    path('admin/product/create', admin_create_product, name='admin_create_product'),
    path('admin/product/get/<int:id>', admin_get_product, name='admin_get_product'),
    path('admin/product/edit/<int:id>', admin_edit_product, name='admin_edit_product'),
    path('admin/product/hide/<int:id>', admin_hide_product, name='admin_edit_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)