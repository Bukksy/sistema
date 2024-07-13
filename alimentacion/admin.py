from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import *

admin.site.register(Restaurante)
admin.site.register(Categoria)
admin.site.register(diariosemanal)
admin.site.register(Producto)
admin.site.register(Profile)
admin.site.register(Reclamo)
admin.site.register(Feedback)

