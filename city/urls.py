from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name = 'landing-page'),
    path('dashboard/<int:pk>', views.dashboard, name = 'dashboard-template'),
]