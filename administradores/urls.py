
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_admin, name='login'),  
    path('admin_view/', views.admin_view, name='admin_view'),  

    path('quanxi_admin/<str:username>/', views.admin_view_quanxi, name='quanxi_admin_view'), 
    path('fuerte_admin/<str:username>/', views.admin_view_fuerte, name='fuerte_admin_view'), 
    path('golozo_admin/<str:username>/', views.admin_view_golozo, name='golozo_admin_view'), 
    path('govegan_admin/<str:username>/', views.admin_view_govegan, name='govegan_admin_view'), 
    path('kushi_admin/<str:username>/', views.admin_view_kushi, name='kushi_admin_view'), 
    path('lagos_admin/<str:username>/', views.admin_view_lagos, name='lagos_admin_view'),
    path('ceaser_admin/<str:username>/', views.admin_view_ceaser, name='ceaser_admin_view'), 
    path('rosa_admin/<str:username>/', views.admin_view_rosa, name='rosa_admin_view'), 
    path('vegano_admin/<str:username>/', views.admin_view_vegano, name='vegano_admin_view'), 
    path('volcanes_admin/<str:username>/', views.admin_view_volcanes, name='volcanes_admin_view'),  
    # VISTAS PARA LOS CRUD DE FUERTE
    path('carga_fuerte', views.carga_fuerte, name='carga_fuerte'),
    path('elimina_producto_fuerte/<int:pk>/', views.elimina_producto_fuerte, name="elimina_producto_fuerte"),
    path('carga_producto_fuerte', views.carga_producto_fuerte, name='carga_producto_fuerte'),
    path('edicion_producto_fuerte/<int:pk>/', views.edicion_producto_fuerte, name='edicion_producto_fuerte'),
    path('editar_producto_fuerte/<int:pk>/', views.editar_producto_fuerte, name='editar_producto_fuerte'),
]