from django.db import models

class Hospitalizations(models.Model):
    HospiPati = models.IntegerField()
    HospiWeeks = models.IntegerField()

    def __str__(self):
        return "{}-{}.format(self.HospiPati, self.HospiWeeks)"
# Create your models here.

