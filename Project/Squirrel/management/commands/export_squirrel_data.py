import csv

from django.core.management.base import BaseCommand
from django.utils import timezone
from Squirrel.models import Squirrel


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file'], 'w') as fp:
            fp.write('X,Y,Unique Squirrel ID,Hectare,Shift,Date,Hectare Squirrel Number,Age,Primary Fur Color,Highlight Fur Color,Combination of Primary and Highlight Color,Color notes,Location,Above Ground Sighter Measurement,Specific Location,Running,Chasing,Climbing,Eating,Foraging,Other Activities,Kuks,Quaas,Moans,Tail flags,Tail twitches,Approaches,Indifferent,Runs from,Other Interactions,Lat/Long,Zip Codes,Community Districts,Borough Boundaries,City Council Districts,Police Precincts\n')
            for data in Squirrel.objects.all():
                for item in data.__dict__:
                    if item not in ['_state', 'id', 'Police_Precincts']:
                        fp.write(str(data.__dict__[item]) + ',')
                    if item == 'Police_Precincts':
                        fp.write(str(data.__dict__[item]) + '\n')
