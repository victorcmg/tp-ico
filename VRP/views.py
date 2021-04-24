from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView

from . models import Problem

class staticView(TemplateView):
   model = Problem

class OrganizationListView(ListView):
    model = Problem