from django.urls import path
from  . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('carrito/', views.carrito, name='carrito'),
    path('menu/', views.menu, name='menu'),
    path('restaurantes/', views.restaurantes, name='restaurantes'),
    
    path('login/', views.login_view, name='login-usuarios'),
    path('signin/', views.signin_view, name='signin'),
    path('logout/', views.logout_view, name='logout'),

    path('perfil/', views.perfil, name='perfil'),
]