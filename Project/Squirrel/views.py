from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Squirrel
from .forms import SquirrelForm

def sightings(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'Squirrel/all.html', context)

def details(request, squirrel_id):
    if request.method == 'POST':
        Squirrel.objects.get(Unique_Squirrel_ID = squirrel_id).delete()
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Squirrel:sightings')
    else:
        squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID = squirrel_id)
        form = SquirrelForm(initial = squirrel.__dict__)
        context = {
            'form': form,
        }
        return render(request, 'Squirrel/detail.html', context)

def add(request):
    #Squirrel.objects.all().delete()
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Squirrel:sightings')
    else:
        form = SquirrelForm()

    context = {
        'form': form,
    }
    return render(request, 'Squirrel/add.html', context)

def stats(request):
    squirrels = Squirrel.objects.all()

    max_Latitude = squirrels[0].Latitude
    min_Latitude = squirrels[0].Latitude

    max_Longitude = squirrels[0].Longitude
    min_Longitude = squirrels[0].Longitude

    list_Highlight_Fur_Color = []

    list_Location = []

    list_Hectare_Squirrel_Number = []

    for item in squirrels:
        if item.Latitude > max_Latitude:
            max_Latitude = item.Latitude
        if item.Latitude < min_Latitude:
            min_Latitude = item.Latitude
        if item.Longitude > max_Longitude:
            max_Longitude = item.Longitude
        if item.Longitude < min_Longitude:
            min_Longitude = item.Longitude

        if item.Highlight_Fur_Color not in list_Highlight_Fur_Color:
            list_Highlight_Fur_Color.append(item.Highlight_Fur_Color)

        if item.Location not in list_Location:
            list_Location.append(item.Location)

        list_Hectare_Squirrel_Number.append(item.Hectare_Squirrel_Number)

    context = {
            'Total_Sightings_Number':len(list_Hectare_Squirrel_Number),
            'max_Latitude': max_Latitude,
            'min_Latitude': min_Latitude,
            'max_Longitude': max_Longitude,
            'min_Longitude': min_Longitude,
            'list_Highlight_Fur_Color': list_Highlight_Fur_Color,
            'list_Location': list_Location,
            'max_Hectare_Squirrel_Number': max(list_Hectare_Squirrel_Number),
            'min_Hectare_Squirrel_Number': min(list_Hectare_Squirrel_Number),
            'avg_Hectare_Squirrel_Number': sum(list_Hectare_Squirrel_Number)/len(list_Hectare_Squirrel_Number),
    }

    return render(request, 'Squirrel/stats.html', context)

def map(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }
    return render(request, 'Squirrel/map.html', context)
