from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Pokemon:
    def __init__(self, name, type, gender, description, level):
        self.name = name
        self.type = type
        self.gender = gender
        self.description = description
        self.level = level

pokemon = [
    Pokemon('Pikachu', 'Electric', 'Make', 'Really bad', 54)
]

def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    return render(request, 'pokemon/index.html', { 'pokemon': pokemon })