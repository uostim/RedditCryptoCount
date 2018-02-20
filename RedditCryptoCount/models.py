from django.db import models
from django.utils import timezone


class LastCount(models.Model):
    coin_id = models.CharField(max_length=256)
    coin_name = models.CharField(max_length=256)
    coin_symbol = models.CharField(max_length=16)
    thiscount = models.IntegerField(null=True, blank=True)
    coin_count = models.IntegerField(null=True, blank=True)
    pc_diff = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    pc_diff_plus_minus = models.CharField(max_length=1, null=True, blank=True)
    lastcount = models.IntegerField(null=True, blank=True)
    lastcount2 = models.IntegerField(null=True, blank=True)
    lastcount3 = models.IntegerField(null=True, blank=True)
    lastcount4 = models.IntegerField(null=True, blank=True)
    lastcount5 = models.IntegerField(null=True, blank=True)
    lastcount6 = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return "{} ({})".format(self.coin_id, self.coin_symbol)


class ThisCount(models.Model):
    coin_id = models.CharField(max_length=256)
    coin_symbol = models.CharField(max_length=16)
    count = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "{} ({})".format(self.coin_id, self.coin_symbol)


class CheckedPosts(models.Model):
    post_title = models.CharField(max_length=301)
