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

def map(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }
    return render(request, 'Squirrel/map.html', context)
