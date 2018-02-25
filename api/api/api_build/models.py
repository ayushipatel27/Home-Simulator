from django.db import models

# Create your models here.
class appliances(models.Model):
    applianceid   = models.IntegerField()
    sensorid      = models.IntegerField()
    powerusage    = models.IntegerField()
    powerrate     = models.IntegerField()
    appliancename = models.CharField(max_length=50)

class dailyusage(models.Model):
    date            = models.DateField()
    totalwaterusage = models.FloatField()
    totalpowerusage = models.IntegerField()
    totalpowercost  = models.DecimalField(max_digits=6, decimal_places=2)
    totalwatercost  = models.DecimalField(max_digits=6, decimal_places=2)
    totalhvacusage  = models.FloatField()
    totalhvaccost   = models.DecimalField(max_digits=6, decimal_places=2)


class energyusage(models.Model):
    timestamp    = models.TimeField()
    sensorid     = models.IntegerField()
    endtimestamp = models.TimeField()
    usage        = models.IntegerField()
    cost         = models.DecimalField(max_digits=6, decimal_places=2)

class hvacusage(models.Model):
    timestamp    = models.TimeField()
    sensorid     = models.IntegerField()
    endtimestamp = models.TimeField()
    usage        = models.FloatField()
    cost         = models.DecimalField(max_digits=6, decimal_places=2)
    temperature  = models.FloatField()

class rooms(models.Model):
    roomid   = models.IntegerField()
    roomname = models.CharField(max_length=50)

class sensors(models.Model):
    sensorid    = models.IntegerField()
    sensorname  = models.CharField(max_length=50)
    sensorstate = models.IntegerField()
    roomid      = models.IntegerField()

class waterusage(models.Model):
    timestamp    = models.TimeField()
    sensorid     = models.IntegerField()
    endtimestamp = models.TimeField()
    usage        = models.FloatField()
    cost         = models.DecimalField(max_digits=6, decimal_places=2)

class weather (models.Model):
    timestamp             = models.TimeField()
    temperature           = models.FloatField()
    precipitation         = models.FloatField()
    chanceofprecipitation = models.FloatField()
    state                 = models.CharField(max_length=50)