from django.shortcuts import render, redirect
from .models import Cat, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm


# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cat_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', {'cats':cats})

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat': cat, 'feeding_form': feeding_form
    })

def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)

class CatCreate(CreateView):
  model = Cat
  fields = "__all__"
  success_url = '/cats/'

class CatUpdate(UpdateView):
  model = Cat
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'
