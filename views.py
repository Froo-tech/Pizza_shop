from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import Order
import os

def index(request):
    return render(request, 'main/index.html')


from .models import Order

def order(request):
    time = os.times()
    # Получаем параметры из URL
    pizza = request.GET.get('pizza')
    drink = request.GET.get('drink')
    toppings = request.GET.get('toppings')
    # Проверка на наличие всех параметров
    if pizza and drink and toppings:
        # Сохраняем данные в БД
        order = Order(
            timeOrder=time,
            pizza=pizza,
            drink=drink,
            toppings=toppings,
        )
        order.save()
        return render(request, 'main/toorder.html')
    else:
        return HttpResponse("Ошибка: Не все параметры были переданы.")

