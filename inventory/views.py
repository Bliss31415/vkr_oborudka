from django.shortcuts import render

def invent_list(request):
    return render(request, 'inventory/invent_list.html', {})