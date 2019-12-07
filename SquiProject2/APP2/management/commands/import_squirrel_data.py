import csv

from django.core.management.base import BaseCommand
from django.utils import timezone
from APP2.models import Squirrel

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        squirrels = []
        for dict_ in data:
            squirrels.append(Squirrel(
                Latitude                                    =  dict_ ['X'],
                Longitude                                   =  dict_ ['Y'],
                Unique_Squirrel_ID                          =  dict_ ['Unique Squirrel ID'],
                Hectare                                     =  dict_ ['Hectare'],
                Shift                                       =  dict_ ['Shift'],
                Date                                        =  dict_ ['Date'],
                Hectare_Squirrel_Number                     =  dict_ ['Hectare Squirrel Number'],
                Age                                         =  dict_ ['Age'],
                Primary_Fur_Color                           =  dict_ ['Primary Fur Color'],
                Highlight_Fur_Color                         =  dict_ ['Highlight Fur Color'],
                Combination_of_Primary_and_Highlight_Color  =  dict_ ['Combination of Primary and Highlight Color'],
                Color_notes                                 =  dict_ ['Color notes'],
                Location                                    =  dict_ ['Location'],
                Above_Ground_Sighter_Measurement            =  dict_ ['Above Ground Sighter Measurement'],
                Specific_Location                           =  dict_ ['Specific Location'],
                Running                                     =  bool(dict_ ['Running']),
                Chasing                                     =  bool(dict_ ['Chasing']),
                Climbing                                    =  bool(dict_ ['Climbing']),
                Eating                                      =  bool(dict_ ['Eating']),
                Foraging                                    =  bool(dict_ ['Foraging']),
                Other_Activities                            =  dict_ ['Other Activities'],
                Kuks                                        =  bool(dict_ ['Kuks']),
                Quaas                                       =  bool(dict_ ['Quaas']),
                Moans                                       =  bool(dict_ ['Moans']),
                Tail_flags                                  =  bool(dict_ ['Tail flags']),
                Tail_twitches                               =  bool(dict_ ['Tail twitches']),
                Approaches                                  =  bool(dict_ ['Approaches']),
                Indifferent                                 =  bool(dict_ ['Indifferent']),
                Runs_from                                   =  bool(dict_ ['Runs from']),
                Other_Interactions                          =  dict_ ['Other Interactions'],
                Lat_Long                                    =  dict_ ['Lat/Long'],
                Zip_Codes                                   =  dict_ ['Zip Codes'],
                Community_Districts                         =  dict_ ['Community Districts'],
                Borough_Boundaries                          =  dict_ ['Borough Boundaries'],
                City_Council_Districts                      =  dict_ ['City Council Districts'],
                Police_Precincts                            =  dict_ ['Police Precincts'], 
            ))

        Squirrel.objects.bulk_create(squirrels)