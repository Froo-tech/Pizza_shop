from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('doorder', order, name="order"),
    path('admin/', admin.site.urls)

]