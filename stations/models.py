# from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length=100)
    neighbors = models.CharField(max_length=500)
    #SQLite doesn't support array fields. If we were using postgres we would model this field like:
    # neighbors = ArrayField( models.ForeignKey(Station, on_delete=models.CASCADE) )
    arrival_popularity = models.FloatField()
    departure_popularity = models.FloatField()
    # size = models.IntegerField() # For when stations limit the number of cars that can arrive and depart a given time
    # train_yard = models.ForeignKey(TrainYard, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
