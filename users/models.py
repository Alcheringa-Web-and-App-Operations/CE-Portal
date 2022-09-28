
from django.db import models
from city.models import City,Competition


class Person(models.Model):
    name = models.CharField(max_length=124)
    contactno=models.CharField(max_length=40,null=True)
    email=models.EmailField(max_length=40,null=True)
    solo = models.BooleanField(default=1)
    
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True,default=None)
    competition= models.ManyToManyField(Competition, blank=True,default=None)
    college_name=models.CharField(max_length=30, blank=True,null=True,default='iitg')
    degree=models.CharField(max_length=5, blank=True,null=True,default='btech')
    gender=models.CharField(max_length=10, blank=True,null=True,default='male')
   
    def __str__(self):
        return f"{self.name} - {self.contactno} - {self.email}"


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Person)
    competition= models.ForeignKey(Competition,on_delete=models.SET_NULL,blank=True, null=True,default='')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True,default=None)

    def __str__(self):
        return self.name