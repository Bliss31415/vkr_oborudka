from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('equipment/', views.equipment_list, name='equipment_list'),
    path('invent_list/', views.invent_list, name='invent_list'),
    #path('<int:item_id>/', views.inventory_detail, name='inventory_detail')
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    # path('signup/', views.signup, name='signup'),
]
