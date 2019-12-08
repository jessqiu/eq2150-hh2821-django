from django.urls import path

from . import views

# Allow for namespaces in reverse URLs
app_name = 'Squirrel'

urlpatterns = [
    path('sightings', views.sightings, name='sightings'),
    
]
