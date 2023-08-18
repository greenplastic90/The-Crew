from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),

  path('crews/', views.CatList.as_view(), name='crew_list'),
]