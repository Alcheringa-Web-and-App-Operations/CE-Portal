from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name = 'landing-page'),
    path('dashboard/<int:pk>', views.dashboard, name = 'dashboard-template'),
    path('my_redirect',views.my_redirect,name="my_redirect"),
    path('sponsors', views.sponsors, name = 'sponsors'),

]