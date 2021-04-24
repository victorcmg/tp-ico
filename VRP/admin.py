from django.contrib import admin
from .models import Problem

@admin.register(Problem)
class PostOrganization(admin.ModelAdmin):            
    list_display = ("name","slug","author","initial_date","num_vehicles","num_store","num_circuit")
    prepopulated_fields = {"slug": ("name",)}