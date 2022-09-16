from django.contrib import admin
from .models import City , Competition, Position

# Register your models here.
admin.site.register(City)
admin.site.register(Position)
admin.site.register(Competition)