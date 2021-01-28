from django.shortcuts import render
from .models import Todohuman
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class Humanlist(ListView):
    template_name = 'list.html'
    model = Todohuman

class Humandetail(DetailView):
    template_name = 'detail.html'
    model = Todohuman

class Humancreate(CreateView):
    template_name = 'create.html'
    model = Todohuman
    fields = (
        'name', 'age', 'job', 'birth', 'memo'
    )
    success_url = reverse_lazy('list')

class HumanUpdate(UpdateView):
    template_name = 'update.html'
    model = Todohuman
    fields = (
        'name', 'age', 'job', 'birth', 'memo'
    )
    success_url = reverse_lazy('list')

class HumanDelete(DeleteView, DetailView):
    template_name = 'delete.html'
    model = Todohuman
    success_url = reverse_lazy('list')