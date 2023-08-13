from django import forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Registration


class RegistrationForm(forms.ModelForm):
    fio = forms.CharField(label="ФИО", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Иванов Иван Иванович'}))
    university = forms.CharField(label="Наименование учебного заведения",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'РГЭУ (РИНХ)'}))
    email = forms.EmailField(label="E-mail",
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.ru'}))
    phone_number = forms.CharField(label="Номер телефона", widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': '+7 (___) ___-__-__'}))

    class Meta:
        model = Registration
        fields = ['fio', 'university', 'email', 'phone_number']
