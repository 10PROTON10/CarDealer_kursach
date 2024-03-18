from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']  # Здесь можно указать поля, по которым будет выполняться поиск в админке

admin.site.register(Customer, CustomerAdmin)