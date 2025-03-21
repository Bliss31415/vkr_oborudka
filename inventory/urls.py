from django.urls import path

from . import views

urlpatterns = [
    path('invent_list/', views.invent_list, name='invent_list'),
]