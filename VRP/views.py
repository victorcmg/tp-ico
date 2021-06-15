from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView , ListView
import json 
import os
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
        
    
    #print(data)
    #print(distances)
    #json_object = json.dumps(new_data, indent = 6)
  
# Serializing json 
    #json_object = json.dumps(data)
       
# Writing to sample.json
    #with open("VRP/static/images/data.json", "w") as outfile:
        #outfile.write(json_object)
    #object_data=[]
    #with open('VRP/static/images/data.json')  as json_file:
    #object_data = json.load(json_file)
        
        new_data = {
        "ID": "1",
        "Algorithm": "a",
        "Vehicles": len(routes),
        "Routes":routes_str,
        "Distance":distances
        }
        #object_data.append(new_data)
    write_json(new_data,'VRP/static/images/data.json')    
    
    return JsonResponse({"dados": new_data}, status=200)

lista=[]
def write_json(data,filename):
    if os.stat(filename).st_size ==0:
        with open(filename,mode='w') as f:
            lista.append(data)
            json.dump(lista,f,indent=4)       
    else:
        
         # ler o ficheiro
        with open(filename,'r') as file:
            dados = json.load(file)
            # actualizar
            dados.append(data)
        #with open(filename,'w') as file:
            #json.dump(data,file, indent=4)
            file.seek(0)
       
        with open(filename,"w") as file:    
        # convert back to json.
            json.dump(dados, file, indent = 4)
             
        #file_data = json.load(file)
        # Join new_dat3a with file_data
        #file_data.update(new_data)
        # Sets file's current position at offset.
        