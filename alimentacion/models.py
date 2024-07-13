from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategorias', primary_key=True)
    nombre_categoria = models.CharField(max_length=50, validators=[MinLengthValidator(1)])

    def __str__(self):
        return str(self.nombre_categoria)

    class Meta:
        db_table = 'categorias'

class diariosemanal(models.Model):
    id_diariosemanal = models.AutoField(db_column='idDiariosemanal', primary_key=True)
    nombre_diariosemanal= models.CharField(max_length=50, validators=[MinLengthValidator(1)])

    def __str__(self):
        return str(self.nombre_diariosemanal)

    class Meta:
        db_table = 'diariosemanal'

class Restaurante(models.Model):
    id_restaurante = models.AutoField(db_column='idRest',primary_key=True)
    imagen_restaurante = models.ImageField(upload_to="alimentacion", null=True)
    nombre_restaurant = models.CharField(max_length=50, validators=[MinLengthValidator(1)])
    descripcion_restaurante = models.CharField(max_length=150, validators=[MinLengthValidator(1)])
    id_categoriarest = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='idCategorias')
    ubicacion_restaurant = models.CharField(max_length=100, validators=[MinLengthValidator(1)])

    def __str__(self):
        return str(self.nombre_restaurant)

    class Meta:
        db_table = 'restaurantes'

class Producto(models.Model):
    id_producto = models.AutoField(db_column='idProd', primary_key=True)
    imagen_producto = models.ImageField(upload_to="alimentacion", null=True)
    nombre_restaurante = models.ForeignKey('Restaurante', on_delete=models.CASCADE, db_column='idRest', default=1)
    categoria_prod = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='idCategorias')
    menusemanal_prod = models.ForeignKey('DiarioSemanal', on_delete=models.CASCADE, db_column='idDiariosemanal')
    nombre_producto = models.CharField(max_length=50, validators=[MinLengthValidator(1)])
    descripcion_producto = models.CharField(max_length=500, validators=[MinLengthValidator(1)])
    precio_producto = models.CharField(max_length=10, validators=[MinLengthValidator(1)])
    cantidad = models.IntegerField()

    def __str__(self):
        return str(self.nombre_producto)

    class Meta:
        db_table = 'productos'

class Profile(models.Model):
    id_profile = models.AutoField(primary_key=True)
    username_saldo = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    saldo = models.IntegerField()

    class Meta:
        db_table = 'profiles'
