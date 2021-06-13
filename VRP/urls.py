# urls.py
from django.urls import path

from VRP.views import TemplateView

from . import views

app_name = 'VRP'

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),   
    path('about/', views.about, name='about'), 

]