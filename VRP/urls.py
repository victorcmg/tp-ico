# urls.py
from django.urls import path

from VRP.views import TemplateView

from . import views

app_name = 'VRP'

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('result/', TemplateView.as_view(template_name='result.html')),   
=======
    path('result/', views.result, name='result'),   
    path('about/', views.about, name='about'), 
>>>>>>> 838c03ff5a0fe3c5c2c41f0a9d0bae90b2e102ac

    path("list/", views.OrganizationListView.as_view(), name="list"),
    path("post/request/ajax", views.ajax_post_view, name="sendJson"),
   
]