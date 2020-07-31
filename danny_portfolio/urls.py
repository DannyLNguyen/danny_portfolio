from django.urls import path     
from . import views
urlpatterns = [
    path('', views.landing),
    path('contact_me', views.contact),
    path('resume', views.resume),
    path('projects', views.projects),
    path('about_me', views.about)		   
]