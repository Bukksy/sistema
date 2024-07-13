from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from alimentacion.models import Producto


class ProductoForm(ModelForm):
	class Meta:
		model = Producto
		fields = ['nombre_producto', 'descripcion_producto', 'nombre_restaurante', 'precio_producto', 'cantidad', 'categoria_prod', 'menusemanal_prod', 'imagen_producto']