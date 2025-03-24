from django.shortcuts import render
from inventory.models import Inventarnik, Inventory_status

def invent_list(request):
    all_invent_info = Inventarnik.objects.all()
    all_invent_status = Inventory_status.objects.all()

    context = {
        'title' : 'Inventory list',
        'all_invent_info' : all_invent_info,
        'all_invent_status' : all_invent_status
    }
    return render(request, 'inventory/invent_list.html', context)