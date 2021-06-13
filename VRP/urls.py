# urls.py
from django.urls import path

from VRP.views import TemplateView

from . import views

app_name = 'VRP'

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.index, name='result'),   
    path('about/', views.index, name='about'), 

]