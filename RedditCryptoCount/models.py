from django.db import models
from django.utils import timezone


class LastCount(models.Model):
    coin_id = models.CharField(max_length=256)
    coin_name = models.CharField(max_length=256)
    coin_symbol = models.CharField(max_length=16)
    lastcount = models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.coin_id, self.coin_symbol)


class TempCount(models.Model):
    coin_id = models.CharField(max_length=256)
    coin_symbol = models.CharField(max_length=16)
    pc_diff = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "{} ({})".format(self.coin_id, self.coin_symbol)
