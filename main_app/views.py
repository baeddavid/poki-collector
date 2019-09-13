from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon
# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', { 'pokemon': pokemon })

def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return render(request, 'pokemon/detail.html', { 'pokemon': pokemon })
