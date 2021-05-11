# urls.py
from django.urls import path

from VRP.views import TemplateView

from . import views

app_name = 'VRP'

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', TemplateView.as_view(template_name='result.html')),   
    path("list/", views.OrganizationListView.as_view(), name="list"),

]