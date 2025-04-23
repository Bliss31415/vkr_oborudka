from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Personal

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'personal/signup.html', {'form': form})

@login_required
def home(request):
    all_personal_info = Personal.objects.all()
    context = {
        'all_personal_info': all_personal_info
    }

    return render(request, 'personal/home.html', context)