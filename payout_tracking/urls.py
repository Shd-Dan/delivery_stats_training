from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_delivery, name='add_delivery'),
    path('delivery/<int:delivery_id>/', views.delivery_details, name='delivery_details'),
    path('courier_details/<str:courier>/', views.courier_details, name='courier_details'),
]
