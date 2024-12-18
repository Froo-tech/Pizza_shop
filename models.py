from django.db import models

class Order(models.Model):
    timeOrder = models.DateTimeField(auto_now_add=True)
    pizza = models.CharField(max_length=100)
    drink = models.CharField(max_length=100)
    toppings = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pizza} with {self.drink} and {self.toppings} at {self.timeOrder}"

class Product(models.Model):
    name = models.CharField(max_length=255)  # Название товара
    quantity = models.PositiveIntegerField()  # Остаток товара
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена товара

    def __str__(self):
        return self.name
