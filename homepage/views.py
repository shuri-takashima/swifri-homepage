from django.shortcuts import render
from django.views import generic
from .models import Art

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class Art_List_View(generic.ListView):
    template_name = './art/list.html'
    model = Art
    ordering = ['-date']

class Art_Detail_View(generic.DetailView):
    template_name = './art/detail.html'
    model = Art
