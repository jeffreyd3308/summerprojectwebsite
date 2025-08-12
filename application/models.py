from django.db import models

# Create your models here.
#admin, weatherweather

class Temperature(models.Model):
    temp = models.DecimalField(default=00.00, max_digits=4, decimal_places=2) #convert all to Fahrenheit
    def __str__(self):
        return str(self.temp)

class Pressure(models.Model):
    pressure = models.IntegerField(default=0)
    def __str__(self):
        return str(self.pressure)

class Humidity(models.Model):
    humidity = models.IntegerField(default=0)
    def __str__(self):
        return str(self.humidity)

class DewPoint(models.Model):
    dewpoint = models.DecimalField(default=00.00, max_digits=4, decimal_places=2)
    def __str__(self):
        return str(self.dewpoint)

class WindSpeed(models.Model):
    wind_speed = models.DecimalField(default=00.00, max_digits=4, decimal_places=2)
    def __str__(self):
        return str(self.wind_speed)

class ActualPrecipitation(models.Model):
    probability = models.DecimalField(default=00.00, max_digits=4, decimal_places=2)
    #negative if provided = false
    def __str__(self):
        return str(self.probability)

class ProvidedActual(models.Model):
    provided = models.BooleanField(default=False)
    #makes probability of rain negative
    #does not allow for error calculations if false
    def __str__(self):
        return str(self.provided)
