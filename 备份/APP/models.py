from django.db import models


# Create your models here.

from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):

    Latitude = models.FloatField()

    Longitude = models.FloatField()

    Unique_Squirrel_ID = models.CharField(
        max_length = 64,
        help_text = _('Unique Squirrel'),
    )

    Hectare = models.CharField(
        max_length = 16,
        help_text = _('Hectare'),
    )

    AM = 'AM'
    PM = 'PM'
    Shift_Choices = (
        (AM, 'AM'),
        (PM, 'PM'),
    )
    Shift = models.CharField(
        max_length = 8,
        help_text = _('AM or PM'),
        choices = Shift_Choices,
    )

    Date = models.CharField(
        max_length = 16,
        help_text = _('Date'),
    )

    Hectare_Squirrel_Number = models.IntegerField()

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Blank = ''
    Age_Choices = (
        (Adult, 'Adult'),
        (Juvenile, 'Juvenile'),
        (Blank, ''),
    )
    Age = models.CharField(
        max_length = 16,
        help_text = _('Adult or Juvenile'),
        choices = Age_Choices,
    )

    Black = 'Black'
    Cinnamon = 'Cinnamon'
    Gray = 'Gray'
    Blank = ''
    Primary_Fur_Color_Choices = (
        (Black, 'Black'),
        (Cinnamon, 'Cinnamon'),
        (Gray, 'Gray'),
        (Blank, ''),
    )
    Primary_Fur_Color = models.CharField(
        max_length = 32,
        help_text = _('Primary Fur Color'),
        choices = Primary_Fur_Color_Choices,
    )

    Highlight_Fur_Color = models.CharField(
        max_length = 64,
        help_text = _('Highlight Fur Color'),
    )

    Combination_of_Primary_and_Highlight_Color = models.CharField(
        max_length = 64,
        help_text = _('Combination of Primary and Highlight Color'),
    )

    Color_notes = models.CharField(
        max_length = 64,
        help_text = _('Color notes'),
    )

    Above_Ground = 'Above Ground'
    Ground_Plane = 'Ground PLane'
    Blank = ''
    Location_Choices = (
        (Above_Ground, 'Abve Ground'),
        (Ground_Plane, 'Ground PLane'),
        (Blank, ''),
    )
    Location = models.CharField(
        max_length = 64,
        help_text = _('Location'),
        choices = Location_Choices,
    )

    Above_Ground_Sighter_Measurement = models.CharField(
        max_length = 32,
        help_text = _('Above Ground Sighter Measurement')
    )

    Specific_Location = models.CharField(
        max_length = 128,
        help_text = _('Specific Location')
    )

    Running = models.BooleanField()

    Chasing = models.BooleanField()

    Climbing = models.BooleanField()

    Eating = models.BooleanField()
    
    Foraging = models.BooleanField()

    Other_Activities = models.CharField(
        max_length = 128,
        help_text = _('Other Activities')
    )

    Kuks = models.BooleanField()

    Quaas = models.BooleanField()

    Moans = models.BooleanField()

    Tail_flags = models.BooleanField()

    Tail_twitches = models.BooleanField()

    Approaches = models.BooleanField()

    Indifferent = models.BooleanField()

    Runs_from = models.BooleanField()

    Other_Interactions = models.CharField(
        max_length = 256,
        help_text = _('Other Interactions')
    )

    Lat_Long = models.CharField(
        max_length = 256,
        help_text = _('Lat/Long')
    )

    Zip_Codes =  models.CharField(
  max_length = 16,
  blank = True
 )

    Community_Districts =  models.CharField(
  max_length = 16,
  blank = True
 )

    Borough_Boundaries =  models.CharField(
  max_length = 16,
  blank = True
 )

    City_Council_Districts =  models.CharField(
  max_length = 16,
  blank = True
 )

    Police_Precincts =  models.CharField(
  max_length = 16,
  blank = True
 )

    def __str__(self):
        return self.Unique_Squirrel_ID
