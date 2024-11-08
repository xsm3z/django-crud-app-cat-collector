from django.shortcuts import render

# Import HttpResponse to send text-based responses
#from django.http import HttpResponse

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class Cat:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description 
    self.age = age

cats = [
    Cat('Lolo', 'tabby', 'Kinda rude.', 3),
    Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
    Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
    Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

def cat_index(request):
  return render(request, 'cats/index.html', {'cats':cats})