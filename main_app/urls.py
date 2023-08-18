from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),

  path('crews/', views.CatList.as_view(), name='crews_list'),
  path('crews/<int:pk>/', views.CrewDetail.as_view(), name='crews_detail'),
  path('crews/create/', views.CrewCreate.as_view(), name='crews_create'),
]