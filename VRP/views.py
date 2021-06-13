from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView , ListView
import json 
from . models import Problem

class staticView(TemplateView):
   model = Problem

class OrganizationListView(ListView):
    model = Problem

def index(response):
    context = {
        "distance1" : 1,
    }

    return render(response,"index.html",context)

def result(response):
    return render(response,"result.html")

def about(response):
    return render(response,"about.html")

def ajax_post_view(request):
    data_from_post = json.load(request)['post_data'] #Get data from POST request
    #Do something with the data from the POST request
    #If sending data back to the view, create the data dictionary
    data = {
        'my_data':data_from_post,
    }
    

    print(data)
    return JsonResponse(data)