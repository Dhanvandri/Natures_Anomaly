from django.db import models
class AnomalyData(models.Model):
    carbon_usage = models.FloatField()
    credits_required = models.FloatField()

