# shop/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")
    icon = models.URLField(blank=True, null=True, verbose_name="Иконка (URL)")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    image = models.URLField(blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        return self.name