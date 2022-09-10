from django.urls import path

from . import views

urlpatterns = [
    path('register-single/', views.register_single, name='register_single'),
    # path('<int:pk>/', views.person_update_view, name='person_change'),
    
    
    # path('ajax/load-competitions/', views.load_competitions, name='ajax_load_competitions'), # AJAX
]