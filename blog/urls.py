from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_shop, name='inventory_shop'),
    path('inventory/list/', views.inventory_list, name='inventory_list'),
    path('inventory/<int:pk>/', views.inventory_detail, name='inventory_detail'),
    path('inventory/new/', views.inventory_new, name='inventory_new'),
    path('inventory/<int:pk>/edit/', views.inventory_edit, name='inventory_edit'),
    path('inventory/<pk>/remove/', views.inventory_remove, name='inventory_remove'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
 
]