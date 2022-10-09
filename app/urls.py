from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug:slug>', views.PRODUCT_DEATIL, name='product_detail'),
    path('url_not_found/', views.url_not_found, name='url_not_found'),
    path('my_account', views.my_accounts, name='my_account'),
    path('my_account/register', views.register, name='handle_register'),
    path('my_account/login', views.LOGIN, name='handle_login'),
    path('accounts/', include('django.contrib.auth.urls')),
    
]
