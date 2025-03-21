from django.shortcuts import render, redirect
from django.contrib import messages


from .models import Personal

def home(request):
    all_personal_info = Personal.objects.all()
    context = {
        'all_personal_info': all_personal_info
    }

    return render(request, 'personal/home.html', context)