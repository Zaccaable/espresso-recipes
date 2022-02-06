from uuid import uuid4
from django.db import models

# Create your models here.
class Coffee(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False),
    name = models.CharField(max_length=100, null=True)
    flavors = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)
    brand = models.CharField(max_length=100, null=True)
    roast = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} / {self.brand}' 


class SuggestedPreparation(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False),
    coffee = models.ForeignKey(Coffee, on_delete=models.SET_NULL, null=True)
    grams_in = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    grams_out = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    extraction_time = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.coffee} / {self.grams_in} -> {self.grams_out}' 


class Basket(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False),
    description = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class Recipe(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False),
    coffee = models.ForeignKey(Coffee, on_delete=models.SET_NULL, null=True)
    basket = models.ForeignKey(Basket, on_delete=models.SET_NULL, null=True)
    grams_in = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    grams_out = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    extraction_time = models.IntegerField(default=0)
    grind_size = models.IntegerField(default=0)
    favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.coffee} / {self.grams_in} -> {self.grams_out}' 