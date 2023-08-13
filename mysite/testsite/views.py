from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm
from .models import Registration


# Create your views here.

def index(request):
    return render(request, 'testsite/index.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            fio = form.cleaned_data['fio']
            university = form.cleaned_data['university']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']

            registration_data = Registration(fio=fio, university=university, email=email, phone_number=phone_number)
            registration_data.save()

            # Редирект на другую страницу после успешной регистрации
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'testsite/register.html', {'form': form})
