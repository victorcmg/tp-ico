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
        distances.append(str(route[1]))
        string_ints = [str(int) for int in route[0]]
        
        str_of_ints = ",".join(string_ints)
        routes_str.append(str_of_ints)
        
    data = {
        "ID": "1",
        "Algorithm": "a",
        "Vehicles": len(routes),
        "Routes":routes_str,
        "Distance":distances
    }
   
    print(data)
    #print(distances)
    #json_object = json.dumps(new_data, indent = 6)
  
# Serializing json 
    #json_object = json.dumps(data)
  
# Writing to sample.json
    #with open("VRP/static/images/data.json", "w") as outfile:
        #outfile.write(json_object)
    #write_json(data,'VRP/static/images/data.json')    
    
    return JsonResponse({'data': 'data'})


def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_dat3a with file_data
        file_data.update(new_data)
        # Sets file's current position at offset.
        #file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 6)