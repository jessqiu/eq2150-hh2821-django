
from django.core.management.base import BaseCommand
import csv
from app.models import Squirrel

class Command(BaseCommand):

        def add_arguments(self, parser):
                 parser.add_argument('csv_file')
        def handle(self, *args, **options):
                 with open(options['csv_file'],'w') as fp:
                     writer = csv.writer(fp)
                     writer.writerow(
                         [
                             'X',
                             'Y',
                             'Unique Squirrel ID',
                             'Shift',
                             'Date',
                             'Age',
                             'Primary Fur Color',
                              'Location',
                             'Specific Location',
                             'Running',
                             'Chasing',
                             'Climbing',
                             'Eating','Foraging','Other Activities',
                             'Kuks','Quaas','Moans','Tail flags','Tail twitches',
                             'Approaches',
                             'Indifferent',
                             'Runs from',
                                                                                                                                                                                                                                                                                                                                                                   ]
                             )
                             squirrel_list = Squirrel.objects.all()
                            for squirrel in squirrel_list:
                                     writer.writerow([
                                         squirrel.Latitude,squirrel.Longitude,
                                        squirrel.Unique_Squirrel_ID,
                                        squirrel.Shift,
                                        squirrel.Date,
                                        squirrel.Age,
                                        squirrel.Primary_Fur_Color,
                                        squirrel.Location,
                                        squirrel.Specific_Location,
                                        squirrel.Running,
                                        squirrel.Chasing,
                                        squirrel.Climbing,squirrel.Eating,squirrel.Foraging,
                                        squirrel.Other_Activities,
                                        squirrel.Kuks,squirrel.Quaas,squirrel.Moans,squirrel.Tail_flags,
                                        squirrel.Tail_twitches,squirrel.Approaches,squirrel.Indifferent
                                                                                                                                                                                                      ])

