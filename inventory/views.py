from django.shortcuts import render, redirect
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

def add_new_invent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        inventory_number = request.POST.get('inventory_number')
        registration_date = request.POST.get('registration_date')
        photo = request.POST.get('photo')
        description = request.POST.get('description')
        status = request.POST.get('status')
        location = request.POST.get('location')

        if name and inventory_number and registration_date and photo and description and status and location:
            Inventarnik.objects.create(
                name=name,
                inventory_number=inventory_number,
                registration_date=registration_date,
                photo=photo,
                description=description,
                status=status,
                location=location
            )
        return redirect('inventory/invent_list.html')
    return render(request,'inventory/add_invent.html')