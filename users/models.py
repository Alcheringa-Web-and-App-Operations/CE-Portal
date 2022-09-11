
from django.db import models
from city.models import City,Competition




# class City(models.Model):
#     name = models.CharField(max_length=40)
   
#     def __str__(self):
#      return self.name
     

# class Competition(models.Model):
#     city = models.ForeignKey(City, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name 


class Person(models.Model):
    name = models.CharField(max_length=124)
    field=models.CharField(max_length=40,null=True)
    Contactno=models.CharField(max_length=40,null=True)
    Email=models.EmailField(max_length=40,null=True)

    
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True,default=None)
    competition= models.ForeignKey(Competition, on_delete=models.SET_NULL, blank=True, null=True,default=None)
   
    def __str__(self):
        return self.name
