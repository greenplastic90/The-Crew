from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Crew
from .forms import CrewForm

# Create your views here.
def home(request):
  
  return render(request, 'home.html')


class CatList(LoginRequiredMixin, ListView):
    model = Crew

class CrewDetail(LoginRequiredMixin, DetailView):
    model = Crew

class CrewCreate(LoginRequiredMixin,CreateView):
    model = Crew
    form_class = CrewForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)