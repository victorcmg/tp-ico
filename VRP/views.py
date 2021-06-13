from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView , ListView
import json 
from . models import Problem
from VRP.routing.vrp import *
from django.views.decorators.csrf import csrf_protect
class staticView(TemplateView):
   model = Problem

class OrganizationListView(ListView):
    model = Problem

def index(response):
    return render(response,"index.html")

<<<<<<< HEAD
@csrf_protect
=======
def result(response):
    return render(response,"result.html")

def about(response):
    return render(response,"about.html")

>>>>>>> 838c03ff5a0fe3c5c2c41f0a9d0bae90b2e102ac
def ajax_post_view(request):
   #  #Get data from POST request
    #Do something with the data from the POST request
    #If sending data back to the view, create the data dictionary
    
<<<<<<< HEAD
    #nome = request.POST.get('data',None)
    
    cordenadas= json.load(request)
   
    print(cordenadas['data'])
    print(cordenadas['num_veiculos'])
    
    routes = get_routes_for_vehicles( cordenadas['data'], cordenadas['num_veiculos'])
    
    print(routes)
    return JsonResponse({'data': 'data'})
=======

    print(data)
    return JsonResponse(data)
>>>>>>> 838c03ff5a0fe3c5c2c41f0a9d0bae90b2e102ac
