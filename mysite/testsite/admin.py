from django.contrib import admin
from .models import Registration


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('fio', 'university', 'email', 'phone_number')  # Отображаемые поля в списке
    search_fields = ('fio', 'university', 'email', 'phone_number')  # Поля для поиска


admin.site.register(Registration, RegistrationAdmin)
# Register your models here.
