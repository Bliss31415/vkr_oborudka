from django.urls import path

from . import views

urlpatterns = [
    path('invent_list/', views.invent_list, name='invent_list'),
    #path('<int:item_id>/', views.inventory_detail, name='inventory_detail')
]
