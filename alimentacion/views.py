from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group 
from django.contrib import messages
import json, re
from .models import *

# Create your views here.

def inicio(request):
    productos_menu_del_dia = Producto.objects.filter(menusemanal_prod__nombre_diariosemanal='Menu del Dia')[:5]
    productos_menu_de_la_semana = Producto.objects.filter(menusemanal_prod__nombre_diariosemanal='Menu de la semana')[:5]
    context = {'productos_menu_del_dia': productos_menu_del_dia, 'productos_menu_de_la_semana':productos_menu_de_la_semana}
    return render(request, 'pages/inicio.html', context)

def menu(request):
    productos =  Producto.objects.all()
    context = {'productos':productos}
    return render(request, 'pages/menu.html', context)

def restaurantes(request):
    restaurant = Restaurante.objects.all()
    context = {'restaurant':restaurant}
    return render(request, 'pages/restaurantes.html', context)

def carrito(request):
    productos_carrito_str = request.GET.get('productos', '[]')

    try:
        productos_carrito = json.loads(productos_carrito_str)
    except json.JSONDecodeError:
        productos_carrito = []

    context = {
        'productos_carrito': productos_carrito
    }
    return render(request, 'pages/carrito.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password, is_admin=False)

        if user is not None:
            login(request, user)
            print(f"Usuario autenticado: {user.username}")  # Imprime el nombre de usuario autenticado
            return redirect('inicio')
        else:
            messages.error(request, 'Credenciales incorrectas. Por favor, intenta nuevamente.')

    return render(request, 'pages/login-usuarios.html')

def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'pages/signin.html', {'error_message': 'El nombre de usuario ya está en uso.'})

        new_user = User.objects.create_user(username=username, email=email, password=password)
        
        new_user.is_admin = False
        
        new_user.is_active = True
        
        new_user.save()
        
        group = Group.objects.get(name='Usuarios') 
        group.user_set.add(new_user)

        login(request, new_user)
        
        return redirect('inicio') 

    return render(request, 'pages/signin.html')

def logout_view(request):
    logout(request)
    return redirect('inicio')