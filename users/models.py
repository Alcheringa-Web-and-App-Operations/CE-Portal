
from email.policy import default
from django.db import models
from city.models import City,Competition


class Person(models.Model):
    name = models.TextField(max_length=124)
    countrycode = models.TextField(max_length = 4, null=True)
    contactno=models.TextField(null=True)
    email=models.EmailField(max_length=40,null=True)
    solo = models.BooleanField(default=1)
    

    city = models.ForeignKey(City, on_delete=models.SET_NULL,default=None,null=True)
    competition= models.ManyToManyField(Competition, null=True,blank=True)
    college_name=models.TextField(max_length=30, blank=True,null=True,default='')
    degree=models.TextField(max_length=10, blank=True,null=True,default='B.Tech')
    gender=models.TextField(max_length=10, blank=True,null=True,default='Male')
    yearofgraduation=models.IntegerField(blank=True, null=True)
   
    def __str__(self):
        return f"{self.name} - {self.contactno} - {self.email}"


class Team(models.Model):
    name = models.TextField(max_length=100)
    members = models.ManyToManyField(Person)
    competition= models.ForeignKey(Competition,on_delete=models.SET_NULL,blank=True, null=True,default='')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True,default=None)

    def __str__(self):
        return self.name