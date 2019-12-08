from django.urls import path

from . import views

# Allow for namespaces in reverse URLs
app_name = 'Squirrel'

urlpatterns = [
    path('sightings', views.sightings, name='sightings'),
    path('sightings/add', views.add, name='add'),
    path('sightings/stats', views.stats, name='stats'),
    path('sightings/<str:squirrel_id>', views.details, name='details'),
    path('map', views.map, name='map'),
]
