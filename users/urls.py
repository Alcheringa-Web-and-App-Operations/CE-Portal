from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    
    
    path('ajax/load-competitions/', views.load_competitions, name='ajax_load_competitions'), # AJAX
]