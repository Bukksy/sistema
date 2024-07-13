from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from alimentacion.models import *
from django.contrib.auth.models import User, Group
from .forms import ProductoForm
def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)

            print(f"Usuario autenticado: {user.username}")
            
            if user.username == 'renato':
                return redirect('admin_view') 
            elif user.username.startswith('Quanxi_Admin'):
                return redirect('quanxi_admin_view', username=username)
            elif user.username.startswith('Fuerte_Admin'):
                return redirect('fuerte_admin_view', username=username)
            elif user.username.startswith('Golozo_Admin'):
                return redirect('golozo_admin_view', username=username)
            elif user.username.startswith('Govegan_Admin'):
                return redirect('govegan_admin_view', username=username)
            elif user.username.startswith('Kushi_Admin'):
                return redirect('kushi_admin_view', username=username)
            
            elif user.username.startswith('Lagos_Admin'):
                return redirect('lagos_admin_view', username=username)
            elif user.username.startswith('Ceaser_Admin'):
                return redirect('ceaser_admin_view', username=username)
            elif user.username.startswith('Rosa_Admin'):
                return redirect('rosa_admin_view', username=username)
            elif user.username.startswith('Vegano_Admin'):
                return redirect('vegano_admin_view', username=username)
            elif user.username.startswith('Volcanes_Admin'):
                return redirect('volcanes_admin_view', username=username)
            
            else:
                return render(request, 'administradores/login.html', {'error_message': 'Acceso no autorizado.'})
        else:
            return render(request, 'administradores/login.html', {'error_message': 'Credenciales inválidas.'})
    return render(request, 'administradores/login.html')

@login_required
def admin_view(request):
    if request.user.username == 'renato' and request.user.is_superuser:
        productos = Producto.objects.all()
        restaurantes = Restaurante.objects.all()
        usuarios = User.objects.all()
        context = {'productos': productos, 'restaurantes': restaurantes, 'usuarios': usuarios}
        return render(request, 'administradores/admin_view.html', context)
    else:
        return redirect('login')

@login_required
def admin_view_quanxi(request, username):
    if request.user.username == username:
        try:
            usuario = User.objects.get(username=username)
            
            restaurante_quanxi = Restaurante.objects.get(nombre_restaurant='Quan Xi')
            productos_quanxi = Producto.objects.filter(nombre_restaurante=restaurante_quanxi)
            
            context = {'productos_quanxi': productos_quanxi}
            return render(request, 'administradores/quanxi/admin_view.html', context)
        
        except User.DoesNotExist:
            return render(request, 'administradores/login.html', {'error_message': 'Usuario no encontrado.'})
    
    else:
        return redirect('login')


@login_required
def admin_view_fuerte(request, username):
    if request.user.username == username:
        try:
            usuario = User.objects.get(username=username)
            restaurante_fuerte = Restaurante.objects.get(nombre_restaurant='El fuerte')
            productos_fuerte = Producto.objects.filter(nombre_restaurante=restaurante_fuerte)
            context = {'productos_fuerte': productos_fuerte}
            return render(request, 'administradores/fuerte/admin_view.html', context)
        except User.DoesNotExist:
            return render(request, 'administradores/login.html', {'error_message': 'Usuario no encontrado.'})
    else:
        return redirect('login')

@login_required
def admin_view_golozo(request, username):
    if request.user.username == username:
        try:
            usuario = User.objects.get(username=username)
            
            restaurante_golozo = Restaurante.objects.get(nombre_restaurant='La picada del golozo')
            productos_golozo = Producto.objects.filter(nombre_restaurante=restaurante_golozo)
            
            context = {'productos_golozo': productos_golozo}
            return render(request, 'administradores/golozo/admin_view.html', context)
        
        except User.DoesNotExist:
            return render(request, 'administradores/login.html', {'error_message': 'Usuario no encontrado.'})
    
    else:
        return redirect('login')


@login_required
def admin_view_govegan(request, username):
    if request.user.username == username:
        try:
            usuario = User.objects.get(username=username)
            restaurante_govegan = Restaurante.objects.get(nombre_restaurant='Go vegan')
            productos_govegan = Producto.objects.filter(nombre_restaurante=restaurante_govegan)
            context = {'productos_govegan': productos_govegan}
            return render(request, 'administradores/govegan/admin_view.html', context)
        except User.DoesNotExist:
            return render(request, 'administradores/login.html', {'error_message': 'Usuario no encontrado.'})
    else:
        return redirect('login')
    

@login_required
def admin_view_kushi(request, username):
    if request.user.username == username:
        try:
            usuario = User.objects.get(username=username)
            
            restaurante_kushi = Restaurante.objects.get(nombre_restaurant='Kushi')
            productos_kushi = Producto.objects.filter(nombre_restaurante=restaurante_kushi)
            
            context = {'productos_kushi': productos_kushi}
            return render(request, 'administradores/kushi/admin_view.html', context)
        
        except User.DoesNotExist:
            return render(request, 'administradores/login.html', {'error_message': 'Usuario no encontrado.'})
    
    else:
        return redirect('login')


@login_required
def admin_view_lagos(request, username):
    if request.user.username == username:
        try:
            usuario = User.objects.get(username=username)
            restaurante_lagos = Restaurante.objects.get(nombre_restaurant='Entre Lagos')
            productos_lagos = Producto.objects.filter(nombre_restaurante=restaurante_lagos)
            context = {'productos_lagos': productos_lagos}
            return render(request, 'administradores/lagos/admin_view.html', context)
        except User.DoesNotExist:
            return render(request, 'administradores/login.html', {'error_message': 'Usuario no encontrado.'})
    else:
        return redirect('login')
    

@login_required
def admin_view_rosa(request, username):
    if request.user.username == username:
        try:
            usuario = User.objects.get(username=username)
            
            restaurante_rosa = Restaurante.objects.get(nombre_restaurant='La nueva rosa')
            productos_rosa = Producto.objects.filter(nombre_restaurante=restaurante_rosa)
            
            context = {'productos_rosa': productos_rosa}
            return render(request, 'administradores/rosa/admin_view.html', context)
        
        except User.DoesNotExist:
            return render(request, 'administradores/login.html', {'error_message': 'Usuario no encontrado.'})
    
    else:
        return redirect('login')

@login_required
def admin_view_ceaser(request, username):
    if request.user.username == username:
        try:
            usuario = User.objects.get(username=username)
            restaurante_ceaser = Restaurante.objects.get(nombre_restaurant='Little Ceaser')
            productos_ceaser = Producto.objects.filter(nombre_restaurante=restaurante_ceaser)
            context = {'productos_ceaser': productos_ceaser}
            return render(request, 'administradores/littleceaser/admin_view.html', context)
        except User.DoesNotExist:
            return render(request, 'administradores/login.html', {'error_message': 'Usuario no encontrado.'})
    else:
        return redirect('login')
    
@login_required
def admin_view_vegano(request, username):
    if request.user.username == username:
        try:
            usuario = User.objects.get(username=username)
            restaurante_vegano = Restaurante.objects.get(nombre_restaurant='Mundo vegano')
            productos_vegano = Producto.objects.filter(nombre_restaurante=restaurante_vegano)
            context = {'productos_vegano': productos_vegano}
            return render(request, 'administradores/vegano/admin_view.html', context)
        except User.DoesNotExist:
            return render(request, 'administradores/login.html', {'error_message': 'Usuario no encontrado.'})
    else:
        return redirect('login')
    
@login_required
def admin_view_volcanes(request, username):
    if request.user.username == username:
        try:
            usuario = User.objects.get(username=username)
            restaurante_volcanes = Restaurante.objects.get(nombre_restaurant='Los Volcanes')
            productos_volcanes = Producto.objects.filter(nombre_restaurante=restaurante_volcanes)
            context = {'productos_volcanes': productos_volcanes}
            return render(request, 'administradores/volcanes/admin_view.html', context)
        except User.DoesNotExist:
            return render(request, 'administradores/login.html', {'error_message': 'Usuario no encontrado.'})
    else:
        return redirect('login')
    
# CRUD PARA PRODUCTOS DE RESTAURANT "FUERTE" WTF esa wea existe?
def carga_fuerte(request):
    return render(request, 'administradores/fuerte/agregar.html')

def elimina_producto_fuerte(request, pk):
    try:
        producto = Producto.objects.get(id_producto=pk)
        producto.delete()
        mensaje = "Artículo eliminado"
    except Producto.DoesNotExist:
        mensaje = "Artículo no existe"

    productos = Producto.objects.all()
    context = {
        'productos': productos,
        'mensaje': mensaje
    }
    return render(request, 'administradores/fuerte/admin_view.html', context)
    
def edicion_producto_fuerte(request, pk):
    producto = get_object_or_404(Producto, id_producto=pk)
    data = {
        'titulo': 'Edicion de producto',
        'noticia': producto,
    }
    return render(request, 'administradores/fuerte/modificar.html', data)

def editar_producto_fuerte(request):
    id_producto = int(request.POST['id'])
    nombre_restaurante = models.ForeignKey('Restaurante', on_delete=models.CASCADE, db_column='idRest', default=1)
    categoria_prod = request.POST['categoria_prod']
    menusemanal_prod = request.POST['menusemanal_prod']
    nombre_producto = request.POST['nombre_producto']
    descripcion_producto = request.POST['descripcion_producto']
    precio_producto = request.POST['precio_producto']
    cantidad = request.POST['cantidad']

    producto = Producto.objects.get(id_producto=id)

    producto.nombre_producto = nombre_producto
    producto.categoria_prod = categoria_prod
    producto.nombre_producto =nombre_producto
    producto.descripcion_producto = descripcion_producto
    producto.precio_producto = precio_producto
    producto.cantidad = cantidad
    

    producto.save()
    return redirect(admin_view_fuerte)


def carga_producto_fuerte(request, producto_id=None):
    if producto_id:  # Verifica si se proporciona un ID de producto
        producto = Producto.objects.get(pk=producto_id)
        form = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    else:
        form = ProductoForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            mensaje = "Producto guardado con éxito"
            return render(request, 'administradores/fuerte/agregar.html', {'mensaje': mensaje, 'form': ProductoForm()})
        else:
            print(form.errors)  # Esto mostrará todos los errores en la consola
            return render(request, 'administradores/fuerte/agregar.html', {'form': form})
    
    return render(request, 'administradores/fuerte/agregar.html', {'form': form})
