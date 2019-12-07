
m django.urls import path

from . import views

# Allow for namespaces in reverse URLs
app_name = 'Jess and Jim'

urlpatterns = [
            path('sightings', views.sightings, name='sightings'),
            ]
