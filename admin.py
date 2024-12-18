from django.contrib import admin
from .models import *  # Импортируем модель Order

# Регистрируем модель Order в админке
admin.site.register(Order)
admin.site.register(Product)