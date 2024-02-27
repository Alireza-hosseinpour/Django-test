from django.db import models

from user.models import User


class Product(models.Model):
    title = models.CharField(max_length=20)
    size = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    weight = models.CharField(max_length=16)
    height = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products',blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    favourites = models.ManyToManyField(User, related_name='favourites', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "products"
        verbose_name_plural = "products"
        db_table = "products"
