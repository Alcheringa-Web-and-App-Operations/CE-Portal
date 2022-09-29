from django.urls import path

from . import views

urlpatterns = [
    path('register-single/', views.register_single, name='register_single'),
    # path('<int:pk>/', views.person_update_view, name='person_change'),
    path('register-team/', views.teamForm, name='register_team'),
    
    
    path('load-competitions-single/', views.load_competitions_single, name='load_competitions_single'),
    path('load-competitions-team/', views.load_competitions_team, name='load_competitions_team'),
    path('load-cities/', views.load_city, name='load_city'), # AJAX
]