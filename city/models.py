from django.db import models
from django.conf import settings

# Create your models here.

class City(models.Model):
    
    cityName = models.CharField(max_length=100)
    venue = models.CharField(max_length = 100, blank = True, null = True)
    cityImage = models.ImageField(default='dcity.jpg',upload_to='city_pics')
    cityCompetitions = models.ManyToManyField('Competition', blank = True, null = True)
    position=models.OneToOneField("Position",on_delete=models.CASCADE, null=True, blank = True)
    competitionDate=models.DateField(null=True)
    cityComp=models.ManyToManyField('CityComp',blank=True)
    comingsoon=models.BooleanField(default=False)
    scheduleImage=models.ImageField(upload_to='schedule_pics',blank=True)
   

    def __str__(self):
        return self.cityName


class Position(models.Model):
    cityName=models.TextField()
    logoTop=models.CharField(max_length=100, blank=True)
    logoLeft=models.CharField(max_length=100, blank=True)
    textTop = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.cityName
    

class CityComp(models.Model):
   competitionId=models.ForeignKey(City, on_delete=models.CASCADE,null=True)
   CompetitionName = models.CharField(max_length=100,null=True)
   competitionDate=models.TimeField(null=True)

   def __str__(self):
        return f"{self.competitionId} - {self.CompetitionName}"


class Competition(models.Model):
    competitionName = models.CharField(max_length=100)
    competitionDescription = models.TextField()
    competitionImage1 = models.ImageField(default='dcomp1.jpg',upload_to='competition_pics')
    competitionImage2 = models.ImageField(default='dcomp2.jpg',upload_to='competition_pics')
    rule_booklet = models.FileField(upload_to='booklets', blank = True)
    background_img=models.ImageField(default='dcity.jpg',upload_to='competition_background_images')
    minimum_user=models.CharField(max_length=1,default='1')
    maximum_user=models.CharField(max_length=2,default='10')


    def __str__(self):
        return self.competitionName 
