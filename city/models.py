from django.db import models

# Create your models here.

class City(models.Model):
    cityName = models.CharField(max_length=100)
    cityImage = models.ImageField(default='dcity.jpg',upload_to='city_pics')
    cityCompetitions = models.ManyToManyField('Competition')
    position=models.OneToOneField("Position",on_delete=models.CASCADE, null=True, blank = True)

    def __str__(self):
        return self.cityName


class Position(models.Model):
    cityName=models.TextField()
    logoTop=models.CharField(max_length=100, blank=True)
    logoLeft=models.CharField(max_length=100, blank=True)
    textTop = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.cityName
    

class Competition(models.Model):
    competitionName = models.CharField(max_length=100)
    competitionDescription = models.TextField()
    competitionImage1 = models.ImageField(default='dcomp1.jpg',upload_to='competition_pics')
    competitionImage2 = models.ImageField(default='dcomp2.jpg',upload_to='competition_pics')

    def __str__(self):
        return self.competitionName
