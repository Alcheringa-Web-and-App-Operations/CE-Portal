from django.urls import path

from . import views

urlpatterns = [
    path('register-single/', views.register_single, name='register_single'),
    # path('<int:pk>/', views.person_update_view, name='person_change'),
    path('team/', views.teamForm, name='register_team'),
    
    
    path('load-competitions/', views.load_competitions, name='load_competitions'),
    path('load-cities/', views.load_city, name='load_city'), # AJAX
]