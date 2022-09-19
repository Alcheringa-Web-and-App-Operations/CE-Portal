from django.contrib import admin
from .models import City, CityComp , Competition, Position

class CompetitionAdmin(admin.StackedInline):
    model =  CityComp
    can_delete = True
    fields = ('competitionId','CompetitionName','competitionDate')
    list_display = ('competitionId','CompetitionName','competitionDate')
    extra=0

    
class DateAdmin(admin.ModelAdmin):
    inlines = [CompetitionAdmin,]

   
# Register your models here.
admin.site.register(City,DateAdmin)
admin.site.register(Position)
admin.site.register(Competition)