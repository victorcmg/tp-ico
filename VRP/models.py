#Import librarys
from django.db import models
from django.contrib.auth.models import User

#represent the problem. the problem are a group of features that characterize the problema
class Problem(models.Model):
    name = models.CharField(max_length=255) #String with max size
    slug = models.SlugField(max_length=255, unique=True) #call the company in url for www.xxx-xxx-xxx.pt
    author = models.ForeignKey(User, on_delete=models.CASCADE)#save the id of the user 
    initial_date = models.DateTimeField(auto_now_add=True)# add a date and a hour the create a new star the program
    time_updated = models.DateTimeField(auto_now_add=True)# add a date and a hour the create a new star the program
    time_executated_start = models.FloatField()
    time_executated_end = models.FloatField()
    time_executation_duration = models.FloatField()
    num_vehicles = models.FloatField()
    num_store = models.FloatField()
    num_circuit =  models.FloatField()

    #call the constructur - created a object 
    def __str__(self):
        return self.name