from django.urls import path     
from . import views
urlpatterns = [
   path('', views.resume),
    path('contact_me', views.contact),
    
    path('projects', views.projects),
    path('about_me', views.about)		   
]