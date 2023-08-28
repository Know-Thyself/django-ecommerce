from django.db import models
from djmoney.models.fields import MoneyField


class Category(models.Model):
    name = models.CharField(max_length=70, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='unbranded')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    price = MoneyField(max_digits=6, decimal_places=2, default_currency='GBP')
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title
