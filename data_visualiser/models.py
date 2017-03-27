from django.db import models


MONTH_CHOICES = (
    ('JAN', 'January'),
    ('FEB', 'February'),
    ('MAR', 'March'),
    ('APR', 'April'),
    ('MAY', 'May'),
    ('JUN', 'June'),
    ('JUL', 'July'),
    ('AUG', 'August'),
    ('SEP', 'September'),
    ('OCT', 'October'),
    ('NOV', 'November'),
    ('DEC', 'December'),
    ) 
    


class Data(models.Model):
    region = models.CharField(max_length = 50) 
    year = models.IntegerField()
    month = models.CharField(max_length=3, choices = MONTH_CHOICES)
    value = models.FloatField(null=True, blank=True)
    
    class Meta:
        abstract = True
    
    
class MaxTempData(Data):
    
    class Meta:
        verbose_name = "Max Temperature Data"
        verbose_name_plural = "Max Temperature Data"
    

class MinTempData(Data):
    class Meta:
        verbose_name = "Min Temperature Data"
        verbose_name_plural = "Min Temperature Data"
    

class MeanTempData(Data):
    class Meta:
        verbose_name = "Mean Temperature Data"
        verbose_name_plural = "Mean Temperature Data"
    


class RainData(Data):
    class Meta:
        verbose_name = "Rain Data"
        verbose_name_plural = "Rain Data"
    

class SunshineData(Data):
    class Meta:
        verbose_name = "Sunshine Data"
        verbose_name_plural = "Sunshine Data"
    

