from django.db import models

# Create your models here.


class Score(models.Model):
    bri = models.FloatField()
    datetime = models.DateTimeField(auto_now_add=True)

    height = models.FloatField()
    waist = models.FloatField()
