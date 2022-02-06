from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from .models import Coffee, Recipe

# Create your views here.
def index(request):
    context = {}

    coffees = Coffee.objects.all()
    recipes = Recipe.objects.all()

    context['coffees'] = coffees
    context['recipes'] = recipes

    return render(request, 'recipes/index.html', context)