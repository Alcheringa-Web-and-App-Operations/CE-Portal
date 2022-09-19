from django.contrib import admin
<<<<<<< HEAD
from .models import City , Competition, Position

# Register your models here.
admin.site.register(City)
=======
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
>>>>>>> master
admin.site.register(Position)
admin.site.register(Competition)