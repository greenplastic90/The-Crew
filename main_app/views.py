from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Crew

# Create your views here.
def home(request):
  
  return render(request, 'home.html')


class CatList(LoginRequiredMixin, ListView):
    model = Crew