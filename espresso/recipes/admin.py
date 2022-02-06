from django.contrib import admin

# Register your models here.
from .models import Coffee, Basket, SuggestedPreparation, Recipe

admin.site.register(Coffee)
admin.site.register(Basket)
admin.site.register(SuggestedPreparation)
admin.site.register(Recipe)