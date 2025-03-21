from django.contrib import admin
from .models import Inventory_status,Inventarnik,Arenda,Teh_obslujiwanie

admin.site.register(Inventory_status)
admin.site.register(Inventarnik)
admin.site.register(Arenda)
admin.site.register(Teh_obslujiwanie)