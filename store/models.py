from django.db import models
from djmoney.models.fields import MoneyField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=70, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])


class Product(models.Model):
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='unbranded')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    price = MoneyField(max_digits=6, decimal_places=2, default_currency='GBP')
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE, null=True
    )

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])

    def get_product_price(self):
        return self.price
