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
]