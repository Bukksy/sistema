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
    path('reclamos/', views.reclamos, name='reclamos'),
    path('feedback/', views.feedback, name='feedback'),

    path('guardar_reclamo/', views.guardar_reclamo, name='guardar_reclamo'),
    path('guardar_feedback/', views.guardar_feedback, name='guardar_feedback'),


    path('metodos/', views.metodos, name='metodos'),
    path('paypal/', views.paypal, name='paypal'),
    path('credito/', views.credito, name='credito'),
    path('debito/', views.debito, name='debito'),
    path('digital/', views.digital, name='digital'),
]