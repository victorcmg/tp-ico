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
    context = {
        "distance1" : 1,
    }

    return render(response,"index.html",context)


@csrf_protect
def result(response):
    return render(response,"result.html")

def about(response):
    return render(response,"about.html")


def ajax_post_view(request):
   #  #Get data from POST request
    #Do something with the data from the POST request
    #If sending data back to the view, create the data dictionary
    

    #nome = request.POST.get('data',None)
    
    cordenadas= json.load(request)
   
   # print(cordenadas['data'])
    #print(cordenadas['num_veiculos'])
    
    routes = get_routes_for_vehicles( cordenadas['data'], cordenadas['num_veiculos'])
    
    print(routes)
    distances = []
    routes_str = []

    for route in routes:
       # distances.push(str(route[1]))
        #string_ints = [str(int) for int in route[0]]
        
        #str_of_ints = ",".join(string_ints)
        #routes_str.push(str_of_ints)
        
        new_data = {
        "Simulation": "1",
        "Algorithm": "a",
        "Vehicles": len(routes),
        "Routes": [str(int) for int in route[0]],
        "Distance": str(route[1]),
        "Map": "mapIcon.png"
    }
   
    print(new_data)
    #print(distances)
    
    return JsonResponse({'data': 'data'})


